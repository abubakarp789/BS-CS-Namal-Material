import requests
import time
import concurrent.futures
from statistics import mean, stdev

BASE_URL = "http://localhost:8080"

def single_request(endpoint, params=None):
    """Make a single request"""
    try:
        start = time.time()
        response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=30)
        end = time.time()
        
        if response.status_code == 200:
            data = response.json()
            return {
                'success': True,
                'response_time': end - start,
                'hostname': data.get('hostname', 'unknown'),
                'execution_time': data.get('execution_time_seconds', 0)
            }
        return {'success': False}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def test_concurrent_requests(num_requests, endpoint='/compute'):
    """Test with concurrent requests"""
    print(f"\n{'='*60}")
    print(f"Testing: {num_requests} concurrent requests to {endpoint}")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(single_request, endpoint, {'n': 500000}) 
                   for _ in range(num_requests)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Analyze results
    successful = [r for r in results if r.get('success')]
    response_times = [r['response_time'] for r in successful]
    hostnames = [r['hostname'] for r in successful]
    
    print(f"\nResults:")
    print(f"  Total Requests: {num_requests}")
    print(f"  Successful: {len(successful)}")
    print(f"  Failed: {num_requests - len(successful)}")
    print(f"  Total Time: {total_time:.2f}s")
    print(f"  Average Response Time: {mean(response_times):.2f}s")
    print(f"  Throughput: {len(successful)/total_time:.2f} req/s")
    print(f"\n  Load Distribution:")
    for hostname in set(hostnames):
        count = hostnames.count(hostname)
        percentage = (count/len(hostnames))*100
        print(f"    {hostname}: {count} requests ({percentage:.1f}%)")
    
    return {
        'total_time': total_time,
        'throughput': len(successful)/total_time,
        'avg_response_time': mean(response_times)
    }

def demonstrate_speedup():
    """Demonstrate speedup from horizontal scaling"""
    print("\n" + "="*60)
    print("SPEEDUP DEMONSTRATION (Amdahl's Law in Practice)")
    print("="*60)
    
    # Test with increasing concurrent load
    test_cases = [1, 2, 4, 8]
    results = {}
    
    for num_requests in test_cases:
        result = test_concurrent_requests(num_requests)
        results[num_requests] = result
        time.sleep(2)  # Cool down between tests
    
    # Calculate speedup
    print("\n" + "="*60)
    print("SPEEDUP ANALYSIS")
    print("="*60)
    baseline_time = results[1]['total_time']
    
    for num_req in test_cases:
        actual_time = results[num_req]['total_time']
        ideal_speedup = num_req
        actual_speedup = baseline_time / (actual_time / num_req)
        efficiency = (actual_speedup / ideal_speedup) * 100
        
        print(f"\n{num_req} concurrent requests:")
        print(f"  Ideal Speedup: {ideal_speedup:.2f}x")
        print(f"  Actual Speedup: {actual_speedup:.2f}x")
        print(f"  Efficiency: {efficiency:.1f}%")
        print(f"  Throughput: {results[num_req]['throughput']:.2f} req/s")

if __name__ == "__main__":
    print("\nWaiting for service to be ready...")
    time.sleep(5)
    
    # Check service health
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✓ Service is ready!\n")
    except:
        print("✗ Service not available. Make sure Docker containers are running.")
        exit(1)
    
    # Run tests
    demonstrate_speedup()