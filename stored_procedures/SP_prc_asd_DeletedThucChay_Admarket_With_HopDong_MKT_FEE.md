# Stored Procedure: `prc_asd_DeletedThucChay_Admarket_With_HopDong_MKT_FEE`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-07-10 14:49:36.123000
- **Ngày sửa cuối**: 2025-07-11 14:21:00.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
/*
	[dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2021-03-24'
*/

CREATE PROCEDURE [dbo].[prc_asd_DeletedThucChay_Admarket_With_HopDong_MKT_FEE]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
	
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan DATETIME = '2025-07-05' --HAIDH COMMENT NGAYDANHSOGIOI HAN CHO VIEC BAT DAU AP DUNG VIEC TINH CHO SAN PHAM MKT-FEE
	
	/*XU LY XOA DU LIEU GHI NHAN THEO REQUEST*/
	--1. THUC HIEN UPDATE TRANG THAI TREN TABLE [ThucChay_PerformanceBase_ThayDoi_HopDong] va [ThucChay_PerformanceBase_ThayDoi]
	--1.1 UPDATE TRANG THAI RECORDSTATUS CUA TABLE ThucChay_PerformanceBase_ThayDoi_HopDong
	UPDATE tctd
	SET tctd.LyDoLoi = N''
	, tctd.RecordStatus =
			(CASE WHEN tctd.RecordStatus IN(1,2) THEN 0 --GHI NHAN THUC CHAY 
				WHEN tctd.RecordStatus IN(6,8) THEN 3   --GHI NHAN THUC CHAY, GHI NHAN THUC CHAY KPI
				WHEN  tctd.RecordStatus IN(5,7) THEN 4  --GHI NHAN THUC CHAY,GHI NHAN THUC CHAY KPI
				ELSE 0
			END)
	FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
	WHERE 1=1 
	AND tctd.NgayThucHien = @NgayThucHien
	AND tctd.LoaiGhiNhan = 2 --LOAI GHI NHAN CHO MKT-FEE

	--HAIDH: CHO NAY CAN XEM LAI
	--AND EXISTS(SELECT TOP (1) ThucChay_PerformanceBase_ThayDoi_ID
	--	FROM dbo.ThucChayDaTinh tcdt
	--	WHERE tcdt.NgayThucHien = @NgayThucHien
	--	AND tcdt.DmHinhThucQuangCao = 5038
	--	AND tcdt.DmSanPhamREF = 817
	--	AND tcdt.DotChayHopDong = N'PerformanceBase_MKT'
	--	AND	tcdt.DotChayBooking = N'Request_TD_PerformanceBase_MKT'
	--	AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
	--	AND tcdt.SoLuongDotChayBooking = tctd.ThucChay_PerformanceBase_ThayDoi_ID
	--	AND tcdt.HopDongID = tctd.HopDongID
	--	AND tcdt.HopDongChiTietREF = tctd.HopDongChitietID
	--)

	--1.2 UPDATE TRANG THAI RECORDSTATUS CUA TABLE ThucChay_PerformanceBase_ThayDoi
	UPDATE td
	SET td.RecordStatus = tdh.RecordStatus
	, td.LyDoTuChoi = tdh.LyDoLoi
	FROM dbo.ThucChay_PerformanceBase_ThayDoi td
	INNER JOIN dbo.ThucChay_PerformanceBase_ThayDoi_HopDong tdh ON td.Id = tdh.ThucChay_PerformanceBase_ThayDoi_ID
	WHERE tdh.NgayThucHien = @NgayThucHien
	AND tdh.DmSanPhamID = 817
	AND tdh.LoaiGhiNhan = 2 --LOAI GHI NHAN CHO MKT-FEE

	--2. THUC HIEN XOA DL TREN THUCCHAYDATINH
	--SELECT tcdt.SoLuongDotChayBooking AS ThucChay_PerformanceBase_ThayDoi_ID
	--, tcdt.HopDongID, tcdt.HopDongChiTietREF 
	--FROM dbo.ThucChayDaTinh tcdt
	--WHERE tcdt.NgayThucHien = @NgayThucHien
	--AND tcdt.DmHinhThucQuangCao = 5038
	--AND tcdt.DmSanPhamREF = 817
	--AND tcdt.DotChayHopDong = N'PerformanceBase_MKT'
	--AND	tcdt.DotChayBooking = N'Request_TD_PerformanceBase_MKT'
	--AND NgayDanhSoHopDong >= @NgayDanhSoGioiHan

	DELETE dbo.ThucChayDaTinh 
	WHERE NgayThucHien = @NgayThucHien
	AND DmHinhThucQuangCao = 5038
	AND DmSanPhamREF = 817
	AND DotChayHopDong = N'PerformanceBase_MKT'
	AND	DotChayBooking = N'Request_TD_PerformanceBase_MKT'
	AND NgayDanhSoHopDong >= @NgayDanhSoGioiHan


	--3. XOA DL TABLE [ThucChay_PerformanceBase_ThayDoi_HopDong]
	DELETE FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	WHERE 1=1 
	AND NgayThucHien = @NgayThucHien
	AND LoaiGhiNhan = 2 --LOAI GHI NHAN CHO MKT-FEE
	/*END XU LY XOA DU LIEU*/


END

```
