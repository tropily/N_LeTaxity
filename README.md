# N\_LeTaxity: NYC Taxi Streaming + Batch Data Pipeline

Welcome to N\_LeTaxity, a production-graded, serverless data engineering platform built on AWS featuring streaming ingestion, batch ETL, and real-time dashboards using NYC Taxi data.

---

## 📊 Project Highlights

* **Python**: Simulation script to emulate live NYC taxi traffic.
* **Kinesis Firehose**: Streaming ingestion of real-time trip data.
* **S3 + AWS Glue + Step Functions**: Batch ingestion and ETL orchestration.
* **S3 Data Lake**: Organized storage into raw/ and processed/ zones.
* **Redshift Serverless**: Centralized analytics warehouse for both streaming and batch data.
* **DynamoDB**: Lightweight control and audit logs for improved pipeline observability and recovery.
* **AWS Step Functions**: End-to-end orchestration of automated ETL workflows.
* **Streamlit**: Real-time dashboard with KPIs, graphs, and streaming vs baseline comparisons.

Note: Streaming operates near-real-time (sub-minute) using Serverless AWS services.

---

## 🗺️ Architecture Diagram

*(Insert your architecture diagram here)*

```markdown
![Architecture Diagram](https://raw.githubusercontent.com/tropily/N_LeTaxity/main/docs/Architecture-Diagram.jpg)
```

---

## 📂 Project Directory Structure

```markdown
├── README.md
├── /scripts
│   ├── streaming_simulator.py
│   └── batch_upload_trigger.py
├── /streamlit_dashboard
│   └── StreamIt_from_redshift_vw.py
├── /glue_jobs
│   └── glue_process_taxi_data.py
├── /lambdas
│   ├── lambda_cleanse_firehose_trip_data.py
│   ├── lambda_trips_copy_to_redshift.py
│   └── other_lambdas.py
├── /infrastructure
│   └── step_functions_definition.json
├── /docs
│   └── architecture_diagram.png
```

---

## 🌐 AWS Services Used

* **Amazon S3** — Data Lake for raw and processed trip data.
* **AWS Glue Data Catalog** — Metadata management for structured querying.
* **AWS Glue ETL** — Batch data transformation.
* **Amazon Kinesis Data Firehose** — Streaming ingestion to S3.
* **AWS Lambda** — Serverless compute for data enrichment and transformation.
* **Amazon Redshift Serverless** — Centralized data warehouse for analytics.
* **AWS Step Functions** — Managed ETL workflow orchestration.
* **Amazon EventBridge** — Scheduled triggers for streaming pipeline refresh.
* **Amazon DynamoDB** — Lightweight control and audit logging for pipelines.
* **Amazon Athena** — Ad-hoc SQL queries directly on S3-based raw/processed data.
* **Streamlit** — Real-time dashboard and KPI visualization.

---

## 📂 Data Sources

* **Historical Data:** Monthly NYC Yellow & Green taxi trip parquet files from [https://www.nyc.gov/](https://www.nyc.gov/)
* **Streaming Data:** Simulated live taxi trip events based on historical data.

---

## 📊 Redshift Key Tables and Views

* `public.taxi_trip_data`: batch cleaned historical data.
* `public.taxi_streaming_trips`: streaming incoming trip data.
* `public.taxi_zone_lookup`: taxi zones lookup.
* `public.taxi_trip_data_vw`: summarized batch trips.
* `public.taxi_streaming_trips_vw`: summarized streaming trips.
* `public.taxi_trip_simulated_today_vw`: simulated today trips for live comparison.
* `public.taxi_trip_top_traffic_vw`: baseline busiest day for benchmarking.

---

## 📈 KPI Metrics in Dashboard

* Trip count
* Total fare revenue
* Average trip delay
* Passengers carried
* Trips per minute
* Real-time vs baseline comparison
* Cumulative trip chart

---

## 📸 Sample Dashboard Screenshot

*(Insert screenshot here)*

---

## 📚 Future Improvements

* Cost optimization: Iceberg tables or Athena for streaming.
* Predictive analytics: model surge demand zones.
* More realistic simulation based on historical patterns.


## 💡 Inspiration

> "Modern Data Engineering: Combining batch + streaming for near real-time decision making."

---

## 💬 Credits

* NYC Taxi public datasets.


---

### 🔗 Connect with me

* LinkedIn: https://www.linkedin.com/in/le-nguyen-v/
* GitHub: https://github.com/tropily/
