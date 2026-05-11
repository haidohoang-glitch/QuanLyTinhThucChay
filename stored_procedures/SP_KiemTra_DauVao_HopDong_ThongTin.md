# Stored Procedure: `KiemTra_DauVao_HopDong_ThongTin`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-23 17:32:26.023000
- **Ngày sửa cuối**: 2016-11-24 10:51:08.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThoiGian` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--DELETE FROM RaSoatThucChayDauVao
--EXEC [KiemTra_DauVao_HopDong_ThongTin] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_ThongTin]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	
	--TRUNCATE TABLE HopDongSyn
	--EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.KiemTra_DauVao_HopDong_Insert
	SET NOCOUNT ON;
	------------------------ngay danh so ------------------------------------------------------
	
	exec [KiemTra_DauVao_HopDong_NgayDS] @ThoiGian
    ----------------------bo phan ------------------------------------------------------
	exec [KiemTra_DauVao_HopDong_Bophan] @ThoiGian
	----------------------Dia diem lam viec ---------------------------
	EXEC [dbo].[KiemTra_DauVao_HopDong_DiaiemLV] @ThoiGian
	----------------------Gia tri hop dong ---------------------------
	EXEC [KiemTra_DauVao_HopDong_GiaTriHD] @ThoiGian
	----------------------DmHinhThucKhachHang--------------------
	EXEC [KiemTra_DauVao_HopDong_HinhThucKH] @ThoiGian
	----------------------DmLoaiKhachHangREF----------------------
	EXEC [KiemTra_DauVao_HopDong_LoaiKH] @ThoiGian
	----------------------MaSoHopDong----------------------
	EXEC [KiemTra_DauVao_HopDong_MaHopDong] @ThoiGian
	----------------------NhanVien----------------------
	EXEC [KiemTra_DauVao_HopDong_NhanVien] @ThoiGian
	----------------------NhanVien----------------------
	EXEC [KiemTra_DauVao_HopDong_Nhom] @ThoiGian
	-----------------------------------------------------------------------------------------------------------------------------------------------------------

	-----------------------------------------------------------------------------------------------------------------------------------------------------------
	SELECT * FROM RaSoatThucChayDauVao


	
END

```
