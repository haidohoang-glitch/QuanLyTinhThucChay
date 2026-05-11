# Table: `Job_desc`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `JOB_NAMES` | `NVARCHAR(200)` nullable |  |
| `JOB_TYPE_NAME` | `SMALLINT` nullable | = 0 là job lấy dữ liệu đầu vào cho tính toán, =1 job thực hiện tính toán thực chạy để đổ vào các table ThucChayDaTinh, ThucChayDaTinhAdmarket,.. |
| `JOB_DESC` | `NVARCHAR(1000)` nullable |  |
| `CREATED_BY` | `NVARCHAR(100)` nullable |  |
| `CREATED_AT` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Job_desc` | `ID` | PRIMARY KEY |
