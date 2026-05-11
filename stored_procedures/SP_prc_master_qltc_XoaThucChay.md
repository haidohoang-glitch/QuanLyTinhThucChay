# Stored Procedure: `prc_master_qltc_XoaThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-10-10 15:26:32.263000
- **Ngày sửa cuối**: 2023-10-10 15:27:40.553000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@idsTcdt` | `nvarchar` | No |
| `@idsTcdtAdmarket` | `nvarchar` | No |
| `@idsTcdtMuaNgoai` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		KhangPV
-- Create date: 03/12/2020
-- Description:	
-- =============================================
CREATE PROCEDURE [dbo].[prc_master_qltc_XoaThucChay] 
	@idsTcdt NVARCHAR(Max),
	@idsTcdtAdmarket NVARCHAR(Max),
	@idsTcdtMuaNgoai NVARCHAR(Max)
AS
BEGIN
    SET NOCOUNT ON;

    -- bang thuc chay da tinh
	IF(@idsTcdt <> '' AND @idsTcdt IS NOT NULL)
    BEGIN
		DELETE dbo.ThucChayDaTinh 
		WHERE ThucChayDaTinhID IN (SELECT [Name] FROM dbo.STRING_SPLIT_QLTC(@idsTcdt))
	END

    -- bảng thuc chay da tinh admarket
	IF(@idsTcdtAdmarket <> '' AND @idsTcdtAdmarket IS NOT NULL)
    BEGIN
		DELETE dbo.ThucChayDaTinhAdmarket
		WHERE ThucChayDaTinhID IN (SELECT [Name] FROM STRING_SPLIT_QLTC(@idsTcdtAdmarket))
	END

    -- bang thuc chay da tinh mua ngoai
	IF(@idsTcdtMuaNgoai <> '' AND @idsTcdtMuaNgoai IS NOT NULL)
	BEGIN
		DELETE dbo.ThucChayDaTinh_MuaNgoai 
		WHERE ID IN (SELECT CONVERT(BIGINT, [Name]) FROM STRING_SPLIT_QLTC(@idsTcdtMuaNgoai))
	END
    
END;









```
