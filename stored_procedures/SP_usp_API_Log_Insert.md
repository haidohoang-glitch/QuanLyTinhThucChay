# Stored Procedure: `usp_API_Log_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-04 10:46:45.303000
- **Ngày sửa cuối**: 2021-03-04 10:46:45.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ApiName` | `nvarchar(4000)` | No |
| `@ApiParams` | `nvarchar` | No |
| `@CallFrom` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[usp_API_Log_Insert]
    -- Add the parameters for the stored procedure here
    @ApiName NVARCHAR(2000),
    @ApiParams NVARCHAR(MAX),
    @CallFrom NVARCHAR(500) = ''
AS
BEGIN
    INSERT INTO dbo.API_Log
    (
        CallFrom,
        CreatedTime,
        API,
        Params,
        IsDeleted
    )
    VALUES
    (   @CallFrom,  -- CallFrom - nvarchar(500)
        GETDATE(),  -- CreatedTime - datetime
        @ApiName,   -- API - nvarchar(2000)
        @ApiParams, -- Params - nvarchar(max)
        0           -- IsDeleted - bit
        );
END;






```
