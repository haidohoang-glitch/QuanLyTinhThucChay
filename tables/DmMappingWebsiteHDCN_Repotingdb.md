# Table: `DmMappingWebsiteHDCN_Repotingdb`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmMappingWebsiteHDCN_ReportingID` | `INT` PK |  |
| `DMWebsiteIdHDCN` | `INT` nullable |  |
| `DMWebsiteIdReportingdb` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmMappingWebsiteHDCN_ReportingID` | `DmMappingWebsiteHDCN_ReportingID` | PRIMARY KEY |
