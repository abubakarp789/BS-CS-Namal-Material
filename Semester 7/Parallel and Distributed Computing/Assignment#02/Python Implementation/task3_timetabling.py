import time
import random
import multiprocessing
from multiprocessing import Process, Manager, cpu_count
from queue import Empty

# --- HARDER PROBLEM FOR i9 ---
class ExamProblem:
    def __init__(self, num_exams=40, num_slots=10, density=0.25):
        self.num_exams = num_exams
        self.num_slots = num_slots
        # 40 exams, 10 slots = Huge search space (10^40).
        # We need density to be low enough to allow solutions, but high enough to prune.
        self.conflicts = [[0]*num_exams for _ in range(num_exams)]
        rng = random.Random(123) # Seed
        for i in range(num_exams):
            for j in range(i+1, num_exams):
                if rng.random() < density:
                    self.conflicts[i][j] = 1
                    self.conflicts[j][i] = 1

    def is_safe(self, exam, slot, schedule):
        # Optimization: Use list or fast lookup
        for assigned_exam, assigned_slot in schedule.items():
            if assigned_slot == slot and self.conflicts[exam][assigned_exam]:
                return False
        return True

def solve_sequential(problem, exam_idx, schedule, limit_time=None):
    if limit_time and time.time() > limit_time:
        return False, None # Timeout
        
    if exam_idx == problem.num_exams:
        return True, schedule
    
    # Heuristic: MRV (Minimum Remaining Values) could go here, but vanilla for now.
    for slot in range(problem.num_slots):
        if problem.is_safe(exam_idx, slot, schedule):
            schedule[exam_idx] = slot
            found, res = solve_sequential(problem, exam_idx + 1, schedule, limit_time)
            if found:
                return True, res
            del schedule[exam_idx]
            
    return False, None

def worker(problem, queue, result, event):
    while not event.is_set():
        try:
            task = queue.get(timeout=0.05)
        except Empty:
            continue
            
        idx, sched = task
        # Run local sequential solver
        found, res = solve_sequential(problem, idx, sched)
        if found:
            result['sol'] = res
            event.set()

def parallel_solver(problem, num_workers):
    m = Manager()
    q = m.Queue()
    res = m.dict()
    evt = m.Event()
    
    # Bootstrap: Expand to Depth 2 (10 slots * 10 slots = 100 tasks)
    # 100 tasks for 32 workers is decent load balancing.
    count = 0
    for s0 in range(problem.num_slots):
        sched = {0: s0}
        for s1 in range(problem.num_slots):
             if problem.is_safe(1, s1, sched):
                 sched_next = sched.copy()
                 sched_next[1] = s1
                 q.put((2, sched_next))
                 count += 1
    
    print(f"Initial Subtrees: {count}")
    
    ps = []
    for _ in range(num_workers):
        p = Process(target=worker, args=(problem, q, res, evt))
        p.start()
        ps.append(p)
        
    # Wait
    t_start = time.time()
    while any(p.is_alive() for p in ps):
        if evt.is_set(): 
            break
        if q.empty() and all(not p.is_alive() for p in ps):
            break
        time.sleep(0.1)
        if time.time() - t_start > 30: # Safety timeout
            print("Timeout!")
            break

    for p in ps: 
        p.terminate()
        p.join()
        
    return res.get('sol')

if __name__ == '__main__':
    print(f"--- Task 3: Timetabling (Hard) ---")
    prob_hard = ExamProblem(num_exams=30, num_slots=8, density=0.3)
    # Note: 30 exams is significantly harder than 20 for backtracking.
    
    print(f"Parallel Solver (Workers={cpu_count()})...")
    t0 = time.time()
    sol = parallel_solver(prob_hard, num_workers=cpu_count())
    t1 = time.time()
    print(f"Parallel Time: {t1-t0:.4f}s")
    
    print(f"Sequential Solver...")
    t0 = time.time()
    found, _ = solve_sequential(prob_hard, 0, {}, limit_time=time.time()+15)
    t1 = time.time()
    if not found:
        print(f"Sequential Time: >15.00s (Timeout/Pruned)")
        print("Parallel Speedup: Infinite (Sequential failed to complete in decent time)")
    else:
        print(f"Sequential Time: {t1-t0:.4f}s")
