# Parallel Computing with Docker Scaling

## Project Demonstrates:

1. **Data Parallelism** - Multiprocessing within application
2. **Task Parallelism** - Load balancing across containers
3. **Horizontal Scaling** - Multiple Docker instances
4. **Speedup Analysis** - Amdahl's Law in practice

## Architecture

*┌─────────────────┐
                │  Load Balancer  │
                │     (NGINX)     │
                └────────┬────────┘
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
 ┌────▼────┐        ┌────▼────┐       ┌────▼────┐
 │  App 1  │        │  App 2  │  ...  │  App N  │
 │ (Flask) │        │ (Flask) │       │ (Flask) │
 └─────────┘        └─────────┘       └─────────┘*

## Quick Start

### 1. Build and Run

```bash
# Build Docker images
docker-compose build

# Start all services (4 instances + load balancer)
docker-compose up -d

# Check status
docker-compose ps
```


### 2. Test the Application

bash

```bash
# Install testing requirements
pip install requests

# Run performance tests
python test_scaling.py
```

### 3. Manual Testing

bash

```bash
# Health check
curl http://localhost:8080/health

# Sequential computation
curl"http://localhost:8080/compute?n=1000000"

# Parallel computation
curl"http://localhost:8080/parallel-compute?n=1000000"

# System stats
curl http://localhost:8080/stats
```

## Scaling Options

### Scale to N instances:

bash

```bash
# Scale to 8 instances
docker-compose up -d --scale app1=2 --scale app2=2 --scale app3=2 --scale app4=2

# Or edit docker-compose.yml and add more services
```

### Monitor Containers:

bash

```bash
# View logs
docker-compose logs -f

# Monitor resources
docker stats
```

## Cleanup

bash

```bash
# Stop all services
docker-compose down

# Remove images
docker-compose down --rmi all
```

## Key Concepts Demonstrated

### 1. Scalability Dimensions

* **Load Scalability** : Handles increasing concurrent requests
* **Horizontal Scaling** : Adding more containers improves throughput

### 2. Types of Parallelism

* **Data Parallelism** : Splitting computation across CPU cores
* **Task Parallelism** : Distributing requests across containers

### 3. Amdahl's Law

* Serial portion: Network overhead, load balancing
* Parallel portion: Request processing
* Test script calculates actual vs ideal speedup

  ## 🎯 Step 6: Run and Test

  ### **Execute Commands:**


  ```bash
  # 1. Build Docker images
  docker-compose build

  # 2. Start services (4 app instances + load balancer)
  docker-compose up -d

  # 3. Verify containers are running
  docker-compose ps

  # 4. Check logs
  docker-compose logs -f

  # 5. Test the application
  pip install requests
  python test_scaling.py

  # 6. Manual testing
  curl http://localhost:8080/
  curl "http://localhost:8080/compute?n=500000"
  curl "http://localhost:8080/parallel-compute?n=500000"

  # 7. Stop everything
  docker-compose down
  ```

---

## 📈 Expected Results

### **Performance Metrics You'll Observe:**

1. **Load Distribution** : Requests evenly distributed across 4 containers
2. **Throughput Improvement** : ~3-4x increase with 4 instances vs 1
3. **Response Time** : Decreases as load spreads across instances
4. **Speedup** : Actual speedup approaching 4x (limited by overhead)

### **Sample Output:**

```
Testing: 8 concurrent requests
  Successful: 8
  Total Time: 2.45s
  Throughput: 3.27 req/s
  
  Load Distribution:
    app_instance_1: 2 requests (25%)
    app_instance_2: 2 requests (25%)
    app_instance_3: 2 requests (25%)
    app_instance_4: 2 requests (25%)

8 concurrent requests:
  Ideal Speedup: 8.00x
  Actual Speedup: 6.53x
  Efficiency: 81.6%
```
