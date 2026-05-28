from flask import Flask, jsonify, request
import time
import math
import os
from multiprocessing import Pool, cpu_count
import socket

app = Flask(__name__)

# Get hostname for identifying which container responds
HOSTNAME = socket.gethostname()
PORT = int(os.environ.get('PORT', 5000))

def compute_intensive_task(n):
    """
    CPU-intensive task: Calculate sum of square roots
    This simulates parallel workload
    """
    result = 0
    for i in range(1, n + 1):
        result += math.sqrt(i) * math.sin(i) * math.cos(i)
    return result

def parallel_compute(data_chunks):
    """
    Parallel computation using multiprocessing
    Demonstrates DATA PARALLELISM
    """
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(compute_intensive_task, data_chunks)
    return sum(results)

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'hostname': HOSTNAME,
        'message': 'Parallel Computing Demo Service',
        'available_endpoints': ['/compute', '/parallel-compute', '/health']
    })

@app.route('/health')
def health():
    """Health check for load balancer"""
    return jsonify({'status': 'healthy', 'hostname': HOSTNAME}), 200

@app.route('/compute')
def compute():
    """
    Sequential computation endpoint
    """
    n = request.args.get('n', default=1000000, type=int)
    
    start_time = time.time()
    result = compute_intensive_task(n)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    return jsonify({
        'hostname': HOSTNAME,
        'computation_type': 'sequential',
        'input_size': n,
        'result': result,
        'execution_time_seconds': round(execution_time, 4),
        'cpu_cores_available': cpu_count()
    })

@app.route('/parallel-compute')
def parallel_compute_endpoint():
    """
    Parallel computation endpoint (DATA PARALLELISM)
    Splits work across CPU cores
    """
    n = request.args.get('n', default=1000000, type=int)
    num_chunks = cpu_count()
    
    # Divide work into chunks for parallel processing
    chunk_size = n // num_chunks
    data_chunks = [chunk_size] * num_chunks
    
    start_time = time.time()
    result = parallel_compute(data_chunks)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    return jsonify({
        'hostname': HOSTNAME,
        'computation_type': 'parallel (data parallelism)',
        'input_size': n,
        'num_chunks': num_chunks,
        'cpu_cores_used': num_chunks,
        'result': result,
        'execution_time_seconds': round(execution_time, 4)
    })

@app.route('/stats')
def stats():
    """System statistics"""
    return jsonify({
        'hostname': HOSTNAME,
        'cpu_cores': cpu_count(),
        'port': PORT
    })

if __name__ == '__main__':
    print(f"Starting server on {HOSTNAME}:{PORT}")
    print(f"Available CPU cores: {cpu_count()}")
    app.run(host='0.0.0.0', port=PORT, debug=False)