\# Grafana Real-Time Monitoring of a Quick-Commerce App



\## 1. Project Overview



This project demonstrates real-time monitoring of a simulated quick-commerce delivery system using \*\*Python, Docker Compose, Prometheus, and Grafana\*\*.



The Python application generates delivery metrics continuously. Prometheus collects these metrics and evaluates alert rules, while Grafana visualizes delivery performance through a live dashboard.



\## 2. Technologies Used



\- \*\*Python\*\* — generates simulated delivery data

\- \*\*Prometheus\*\* — collects metrics and evaluates alert rules

\- \*\*Grafana\*\* — visualizes metrics through dashboard panels

\- \*\*Docker and Docker Compose\*\* — build and run the services

\- \*\*PromQL\*\* — queries monitoring metrics



\## 3. Project Architecture



1\. The Python application simulates total deliveries, pending deliveries, deliveries on the way, and delivery times.

2\. The application exposes metrics on port `8000`.

3\. Prometheus scrapes the metrics every 5 seconds.

4\. Prometheus evaluates configured alert rules.

5\. Grafana connects to Prometheus as its data source and displays real-time metrics.



\## 4. Project Structure



```text

Grafana-Realtime-Monitoring-of-Quick-Commerce-App/

├── delivery\_metrics.py

├── requirements.txt

├── Dockerfile

├── compose.yaml

├── prometheus/

│   ├── prometheus.yml

│   └── alert\_rules.yml

└── grafana/

&#x20;   └── provisioning/

&#x20;       └── datasources/

&#x20;           └── prometheus.yml

```



\## 5. Metrics Monitored



| Metric | Description |

|---|---|

| `total\_deliveries` | Total simulated deliveries |

| `pending\_deliveries` | Deliveries awaiting completion |

| `on\_the\_way\_deliveries` | Deliveries currently on the way |

| `average\_delivery\_time\_sum` | Sum of observed delivery times |

| `average\_delivery\_time\_count` | Number of delivery-time observations |



The application generates new values every 5 seconds.



\## 6. Alert Rules



\### High Pending Deliveries

\- Expression: `pending\_deliveries > 10`

\- Duration: 15 seconds

\- Severity: Warning



\### High Average Delivery Time

\- Expression: `(average\_delivery\_time\_sum / average\_delivery\_time\_count) > 30`

\- Duration: 15 seconds

\- Severity: Critical



The pending-delivery alert was tested by temporarily increasing the simulated pending-delivery values. Prometheus confirmed that `HighPendingDeliveries` entered the `firing` state. The application was subsequently restored to its normal simulation range of 1–15 pending deliveries.



\## 7. Setup and Execution



\### Prerequisites

\- Docker Desktop installed and running

\- Docker Compose available through the Docker CLI



\### Start the application



From the project directory, run:



```powershell

docker compose up -d --build

```



\### Check running services



```powershell

docker compose ps

```



\### View application logs



```powershell

docker logs --tail 20 delivery\_metrics

```



\### Stop the services



```powershell

docker compose down

```



\## 8. Access the Services



| Service | URL |

|---|---|

| Delivery metrics endpoint | http://localhost:8000/metrics |

| Prometheus | http://localhost:9090 |

| Prometheus targets | http://localhost:9090/targets |

| Prometheus alerts | http://localhost:9090/alerts |

| Grafana | http://localhost:3000 |



Grafana's default credentials for a fresh installation are commonly `admin` / `admin`; use the credentials configured for your installation if they have been changed.



\## 9. Sample PromQL Queries



Total deliveries:



```promql

total\_deliveries

```



Pending deliveries:



```promql

pending\_deliveries

```



Deliveries on the way:



```promql

on\_the\_way\_deliveries

```



Average delivery time in seconds:



```promql

average\_delivery\_time\_sum / average\_delivery\_time\_count

```



\## 10. Results



\- Successfully ran the Python application, Prometheus, and Grafana using Docker Compose.

\- Verified that Prometheus targets were healthy.

\- Connected Grafana to Prometheus successfully.

\- Created dashboard panels for delivery metrics.

\- Verified the pending-delivery alert in the `firing` state.

\- Restored the normal delivery simulation after alert testing.



\## 11. Screenshots



The `screenshots/` directory contains evidence of the Grafana data source, dashboard metrics, Prometheus alert, and running Docker services.



\## 12. Conclusion



This project demonstrates how containerized applications can be monitored using Prometheus and Grafana. It provides real-time metric collection, visualization, and threshold-based alerting for a simulated quick-commerce delivery workflow.



