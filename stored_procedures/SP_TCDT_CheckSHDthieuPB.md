# Stored Procedure: `TCDT_CheckSHDthieuPB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-08 15:50:40.280000
- **Ngày sửa cuối**: 2024-03-08 15:50:40.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[TCDT_CheckSHDthieuPB]
    -- Add the parameters for the stored procedure here
    @Ngaythuchien DATETIME
 
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
 SET NOCOUNT ON;
 SELECT contract_number,username,phanbo,dbo.FormatNumber(isnull(sum(CONVERT(FLOAT,domain_tt_money)),0)) AS TC_KVAT, NgayThucHien 
 FROM dbo.ThucChayAdmarket_PhanBo  WHERE NgayThucHien= @Ngaythuchien
 AND ISNULL(contract_number,'') <> N'' 
 AND contract_number <> N'BLANK'
 AND phanbo=0
 GROUP BY  username,NgayThucHien,phanbo,contract_number
 ORDER BY NgayThucHien
END;

```
