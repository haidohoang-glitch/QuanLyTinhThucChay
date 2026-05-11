# Stored Procedure: `KiemTra_DauVao_ThongTinTienVe_KeyID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:30:04.543000
- **Ngày sửa cuối**: 2016-11-22 10:30:14.933000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThongTinTienVe_KeyID]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.

	TRUNCATE TABLE ThongTinTienVeSyn

	INSERT INTO ThongTinTienVeSyn
	EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.[KiemTra_DauVao_ThongTinTienVe_Insert]

	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThongTinTienVeID FROM ABM_Data_ThucChay.dbo.ThongTinTienVe
	)A
	FULL OUTER JOIN 
	(
	SELECT id  FROM  ThongTinTienVeSyn
	)B
	ON A.ThongTinTienVeID =B.id
	--AND A.HopDongREF = B.hd_id
	WHERE A.ThongTinTienVeID IS NULL OR B.id IS NULL
	 --OR A.HopDongREF IS NULL OR B.hd_id IS NULL
    
END

```
