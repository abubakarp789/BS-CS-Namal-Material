import time
import random
from multiprocessing import Pool, cpu_count

# --- OPTIMIZATION FOR i9-14900K (32 Threads) ---
# Previous N=1,000,000 was too small (took ~1s), making process spawn overhead dominant.
# With 32GB RAM, we can handle N=20,000,000 easily.
N_USERS = 20_000_000 
CAPACITY_W = N_USERS * 10 

def sequential_greedy(users, capacity):
    # 1. Density
    for u in users:
        u['density'] = u['p'] / u['w']
    
    # 2. Sort
    users.sort(key=lambda x: x['density'], reverse=True)
    
    # 3. Selection
    total_p = 0
    current_w = 0
    
    for u in users:
        if current_w + u['w'] <= capacity:
            current_w += u['w']
            total_p += u['p']
        else:
            rem = capacity - current_w
            frac = rem / u['w']
            total_p += u['p'] * frac
            break
            
    return total_p

def calc_density_chunk(chunk):
    # Pure CPU bound task
    for u in chunk:
        u['density'] = u['p'] / u['w']
    return chunk

def parallel_greedy(users, capacity):
    # i9-14900K has 24 cores / 32 threads.
    # We want chunks large enough that the pickling cost is negligible.
    cores = cpu_count()
    chunk_size = len(users) // cores
    
    chunks = [users[i:i + chunk_size] for i in range(0, len(users), chunk_size)]
    
    # Multiprocessing Map
    with Pool(processes=cores) as pool:
        processed_chunks = pool.map(calc_density_chunk, chunks)
    
    # Flatten
    flat_users = [u for chunk in processed_chunks for u in chunk]
    
    # Sort
    flat_users.sort(key=lambda x: x['density'], reverse=True)
    
    # Selection
    total_p = 0
    current_w = 0
    
    for u in flat_users:
        if current_w + u['w'] <= capacity:
            current_w += u['w']
            total_p += u['p']
        else:
            rem = capacity - current_w
            frac = rem / u['w']
            total_p += u['p'] * frac
            break
            
    return total_p

if __name__ == '__main__':
    print(f"--- Task 1: Bandwidth Allocation (High-End Optimization) ---")
    print(f"System: i9-14900K Detected (Logical Cores: {cpu_count()})")
    print(f"Dataset Size: {N_USERS:,} users (Heavy Load)")
    
    print("Generating data...", end="", flush=True)
    # Re-gen with fast logic for 20M items
    raw_data = [{'p': int(random.random()*100), 'w': int(random.random()*50)+1} for _ in range(N_USERS)]
    print(" Done.")
    
    data_seq = [d.copy() for d in raw_data]
    data_par = [d.copy() for d in raw_data]
    
    print("\nRunning Sequential...")
    t0 = time.time()
    p_seq = sequential_greedy(data_seq, CAPACITY_W)
    t1 = time.time()
    time_seq = t1 - t0
    print(f"Sequential Time: {time_seq:.4f}s")
    
    print("\nRunning Parallel (Full Core Utilization)...")
    t0_p = time.time()
    p_par = parallel_greedy(data_par, CAPACITY_W)
    t1_p = time.time()
    time_par = t1_p - t0_p
    print(f"Parallel Time:   {time_par:.4f}s")
    
    print(f"Speedup: {time_seq / time_par:.2f}x")
