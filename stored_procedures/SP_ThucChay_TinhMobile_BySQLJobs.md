# Stored Procedure: `ThucChay_TinhMobile_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-23 09:36:10.493000
- **Ngày sửa cuối**: 2024-11-27 10:29:48.343000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
 --=============================================	
-- EXEC [ThucChay_TinhMobile_BySQLJobs]
--
CREATE PROCEDURE [dbo].[ThucChay_TinhMobile_BySQLJobs]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	SET NOCOUNT ON;

    DECLARE @StartDate	DATETIME,
			@EndDate	DATETIME
			
	SET @StartDate = (
		SELECT top (1) (tcdt.NgayThucHien)
		-- MAX(tcdt.NgayThucHien)
		FROM dbo.ThucChayDaTinh AS tcdt
		LEFT JOIN 
		(SELECT * FROM dbo.HopDongChiTiet hdct 
			WHERE hdct.DeletedStatus = 0 
			AND hdct.DmSanPhamREF = 342
			AND ISNULL(hdct.DmLoaiNenTangREF,0) <> 8
		)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
		WHERE tcdt.DmSanPhamREF = 342
		AND NOT (tcdt.DmHinhThucQuangCao in (13,42) or tcdt.DmLoaiBannerREF in (17,18))
		AND (tcdt.DotChayHopDong NOT in ( N'NGAY', N'CPM_DonViGoi'))
		ORDER BY tcdt.NgayThucHien desc
	)

	SET @StartDate = DATEADD(dd, 1, @StartDate);	
	SET @StartDate = CONVERT(DATE, @StartDate)
	SET @EndDate = CONVERT(DATE,GETDATE());
	SET @EndDate = DATEADD(dd,-1,@EndDate);

	-----dat chay de fix loi ngay 06/06/2022
	--SET @StartDate = '2022-06-01'
	--SET @EndDate =   '2022-06-05'

	---- Tinh thuc chay Mobile  --
	--SET @StartDate = '2018-12-06'
	--SET @EndDate =   '2018-12-06'
	--EXEC dbo.ThucChay_ExcInsertThucChayDaTinhMobile_v4 @StartDate, @EndDate
	
	------ Update Gia tri thay doi thuc chay Mobile
	--EXEC dbo.ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_v2 @StartDate, @EndDate
	
	------Cap Nhat Thong tin nhan hang loi
	----EXEC ThucChay_UpdateThongTinNhanHangThucChayDaTinh @EndDate

	EXEC sp_TC_ExcInsertThucChayDaTinh_Mobile @StartDate, @EndDate, NULL
	
		
END


```
