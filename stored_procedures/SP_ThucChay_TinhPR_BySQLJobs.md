# Stored Procedure: `ThucChay_TinhPR_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-02 13:33:07.637000
- **Ngày sửa cuối**: 2024-11-27 14:44:08.490000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [ThucChay_TinhPR_BySQLJobs]
*/
CREATE PROCEDURE [dbo].[ThucChay_TinhPR_BySQLJobs]
	
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	
	SET @dtStart = (
						SELECT TOP(1) NgayThucHien FROM dbo.ThucChayDaTinh
						WHERE DmSanPhamREF IN (141,245,250,637,305)
						AND NOT (DmHinhThucQuangCao IN (42, 13) or DmLoaiBannerREF = 18)
						ORDER BY NgayThucHien DESC
					)
	
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)	

	--Tinh Thuc Chay PR
	SET @dtStart = DATEADD(dd,1, @dtStart)
	SET @dtStart = CONVERT(date, @dtStart)
	SET @dtEnd = CONVERT(date, @dtEnd)

	--HAIDH COMMENT PHUONG PHAP TINH CU LAI VI NO CHAY LÀM TREO HE THONG 20220114
	--PRINT 'Exe sp_TC_InsertThucChayDaTinh_PR: '	+ CONVERT(NVARCHAR(20),GETDATE(),120)
	--EXEC [sp_TC_InsertThucChayDaTinh_PR] @dtStart, @dtEnd, NULL

	--PRINT 'END Exe sp_TC_InsertThucChayDaTinh_PR: '	+ CONVERT(NVARCHAR(20),GETDATE(),120)
	----Tinh gia tri thay doi PR
	--PRINT 'Exe sp_TC_TinhGiaTriThayDoi_PR'
	--EXEC [sp_TC_TinhGiaTriThayDoi_PR] @dtStart,@dtEnd

	----------------------------MAPPING HDCT 2020-01-01------------------------------------------------
	PRINT N'Tính giá trị thay đôi cho PR theo phương pháp mapping HopDongChiTiet từ HD NgayDanhSo >= 2020-01-01: '	+ CONVERT(NVARCHAR(20),GETDATE(),120)
	EXEC [dbo].[sp_ThucChay_CheckTTTD_ThongTinTreoThayDoi_PR_HDCT] 
			@NgayThucHien = @dtStart ,
			@ThoiGianBDTinh = '2019-12-31'

	PRINT N'Tính GTTD khi HD hoặc HDCT PR hủy theo phương pháp mapping HopDongChiTiet từ HD NgayDanhSo >= 2020-01-01: '	+ CONVERT(NVARCHAR(20),GETDATE(),120)
	EXEC [dbo].[sp_ThucChay_CheckTTTD_HopDongOrHopDongChiTietHuy_PR_HDCT] 
			@NgayThucHien = @dtStart ,
			@ThoiGianBDTinh = '2019-12-31'
	PRINT 'Finish: '	+ CONVERT(NVARCHAR(20),GETDATE(),120)

	PRINT N'Tính thực chạy cho PR theo phương pháp mapping HopDongChiTiet từ HD NgayDanhSo >= 2020-01-01: '	+ CONVERT(NVARCHAR(20),GETDATE(),120)
	EXEC [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_PR_HDCT]
			@StartDate = @dtStart ,
			@EndDate = @dtEnd ,
			@piHopDongID = NULL

	
END
```
