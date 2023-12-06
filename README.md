# Pager Service Project : Aircall-tech-test

## Overview
This project implements the domain logic for a Pager Service that is part of an Alert Notification System. The Pager Service handles alerts from monitored services and sends notifications according to defined escalation policies. We're using `SOLID principles`.

## Concurrency Considerations
The system is designed to prevent sending multiple notifications to the same target for concurrent alerts. If two alerts are received simultaneously, the Pager Service will send only one notification per target, per alert.

## Database Guarantees (Hypothetical)
Even though database persistence is not implemented in this exercise, the following guarantees would be expected from a database supporting this system:

- Atomicity: Operations on the database are atomic, ensuring that notifications are either fully processed or not at all.
- Consistency: The database maintains a consistent state, ensuring that all notification rules are applied correctly.
- Isolation: Concurrent transactions are isolated from each other, preventing double notifications.
- Durability: Once a notification transaction is completed, it is permanently stored in the database.

## Running Tests

To run the unit tests for this project, follow these steps:

1. **Create a Python environment** (optional if you already have a suitable environment):
```bash
   conda create --name aircall_env python=3.8
```


2. **Activate the environment:**

```bash

conda activate aircall_env
```

3. **Install required libraries:**

```bash

pip install -r requirements.txt
```

4. **Run tests:**
Navigate to the project's root directory, where the tests folder is located. Then run the following command:

```bash

python -m unittest discover tests
```