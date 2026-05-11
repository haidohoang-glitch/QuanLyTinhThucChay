# Stored Procedure: `prc_asd_QLCN_GetListNgayThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-06-27 17:34:06.723000
- **Ngày sửa cuối**: 2023-06-27 17:34:06.723000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ContractIds` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--ABM_Data_ThucChay.prc_asd_QLCN_GetListNgayThucChay
CREATE PROCEDURE [dbo].[prc_asd_QLCN_GetListNgayThucChay]
	-- Add the parameters for the stored procedure here
	@ContractIds NVARCHAR(Max) = ''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	--DECLARE @ContractIds NVARCHAR(Max) = '32302,32387,39076,39083';
    -- Insert statements for procedure here
	SELECT HopDongID, MIN(NgayThucHien) AS 'NgayThucHien' FROM [ABM_Data_ThucChay].[dbo].[ThucChayDaTinh] 
	WHERE HopDongID IN (SELECT [value] FROM STRING_SPLIT(@ContractIds,','))
	GROUP BY HopDongID
END

```
