# Stored Procedure: `KiemTra_DauVao_HopDongAttachFile_TenFile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:24:53.290000
- **Ngày sửa cuối**: 2016-11-22 10:24:53.290000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongAttachFile_TenFile]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongAttachFileID,[fileName] FROM ABM_Data_ThucChay.dbo.HopDongAttachFile
	)A
	FULL OUTER JOIN 
	(
	SELECT id,fileName FROM HopDongAttachFileSyn 
	)B
	ON A.HopDongAttachFileID =B.id
	AND A.fileName = B.fileName
	WHERE A.HopDongAttachFileID IS NULL OR B.id IS NULL OR A.fileName IS NULL OR B.fileName IS NULL
    
END

```
