# Stored Procedure: `KiemTra_DauVao_HopDongAttachFile_LoaiFile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:24:16.210000
- **Ngày sửa cuối**: 2016-11-22 10:24:16.210000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongAttachFile_LoaiFile]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	TRUNCATE TABLE HopDongAttachFileSyn

	INSERT INTO HopDongAttachFileSyn
	EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.[dbo].[KiemTra_DauVao_HopDongAttachFile_Insert] 
			
	SELECT A.*, B.* FROM (
	SELECT HopDongAttachFileID,FileTypeREF FROM ABM_Data_ThucChay.dbo.HopDongAttachFile
	)A
	FULL OUTER JOIN 
	(
	SELECT id,filetypeID FROM HopDongAttachFileSyn 
	)B
	ON A.HopDongAttachFileID =B.id
	AND A.FileTypeREF = B.filetypeID
	WHERE A.HopDongAttachFileID IS NULL OR B.id IS NULL OR A.FileTypeREF IS NULL OR B.filetypeID IS NULL
    
END

```
