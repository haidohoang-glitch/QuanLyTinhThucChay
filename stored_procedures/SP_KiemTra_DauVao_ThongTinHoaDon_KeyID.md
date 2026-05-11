# Stored Procedure: `KiemTra_DauVao_ThongTinHoaDon_KeyID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:47:07.157000
- **Ngày sửa cuối**: 2016-11-22 10:47:07.157000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThongTinHoaDon_KeyID]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.

	TRUNCATE TABLE ThongTinHoaDonSyn

	INSERT INTO ThongTinHoaDonSyn
	EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.[KiemTra_DauVao_ThongTinHoaDon_Insert] 

	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThongTinHoaDonID FROM ABM_Data_ThucChay.dbo.ThongTinHoaDon
	)A
	FULL OUTER JOIN 
	(
	SELECT id  FROM  ThongTinHoaDonSyn 
	)B
	ON A.ThongTinHoaDonID =B.id
	--AND CONVERT (DATE,A.NgayThanhToan) = CONVERT (DATE,B.ngaythanhtoan)
	WHERE A.ThongTinHoaDonID IS NULL OR B.id IS NULL
	 --OR A.NgayThanhToan IS NULL OR B.ngaythanhtoan IS NULL
    
END

```
