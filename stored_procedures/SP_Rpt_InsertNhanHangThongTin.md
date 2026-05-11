# Stored Procedure: `Rpt_InsertNhanHangThongTin`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:33.063000
- **Ngày sửa cuối**: 2015-03-13 13:21:07.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[Rpt_InsertNhanHangThongTin] 
	@NgayThucHien DATETIME
AS
BEGIN
	--delete du lieu
	DELETE FROM RptNhanHangThongTinChung
	WHERE Convert(date,NgayThucHien) = @NgayThucHien
	
	--insert data
	INSERT INTO RptNhanHangThongTinChung
	  (
	    DmNhanHangREF,
	    TenNhanHang,
	    DmNganhHangREF,
	    TenNganhHang,
	    KhachHangSoHuuREF,
	    TenKhachHangSoHuu,
	    MaSoThue,
	    DiaChi,
	    SoDienThoai,
	    TongDoanhSoKyHaiDau,
	    TongDoanhSoThucChay,
	    ViTriNhanHangInNganh,
	    ViTriNhanHangInAdmicro,
	    DSNhanSoVoiTBNganh,
	    TinhTrangNhanHang,
	    NgayThucHien,
	    HopDongChiTietREF,
	    CreatedBy,
	    CreatedAt,
	    LastModifiedBy,
	    LastModifiedAt,
	    RecordStatus,
	    DeletedStatus
	  )
	SELECT dnh.DmNhanHangID,
	       dnh.TenNhanHang,
	       dnh.DmNghanhHangREF,
	       'tennganhhang' tennganhhang,
	       dnh.DmKhachhangSohuuREF,
	       dnh.TenKhachHang,
	       dnh.MaSoThue,
	       dnh.DiaChiKhachHang,
	       dnh.SoDienThoai,
	       rptc.TongDoanhSoKyHaiDau,
	       rptc.TongDoanhSoThucChay,
	       0 ViTriNhanHangInNganh,
	       0 ViTriNhanHangInAdmicro,
	       0 DSNhanSoVoiTBNganh,
	       1 TinhTrangNhanHang
	       , rptc.NgayThucHien,
	       '' HopDongChiTietREF,
	       'ABM_nhan',
	       GETDATE(),
	       'ABM_nhan',
	       GETDATE(),
	       0,
	       0
	FROM   
	(		select dnh.DmNhanHangID, dnh.TenNhanHang, dnh.DmNghanhHangREF, isnull(dnh.DmKhachhangSohuuREF,0)DmKhachhangSohuuREF
			, isnull(khf.TenKhachHang,'')TenKhachHang
			, isnull(khf.MaSoThue,'')MaSoThue
			, isnull(khf.DiaChiKhachHang,'')DiaChiKhachHang
			, isnull(khf.SoDienThoai,'')SoDienThoai
			from DmNhanHang dnh
			LEFT JOIN KhachHangThongTinChung khf
	            ON  dnh.DmKhachhangSohuuREF = khf.KhachHangThongTinChungID
	 		WHERE dnh.DeletedStatus <> 1
	 )dnh          
	 INNER JOIN 
	 (
            SELECT SUM(ct.TongDoanhSoKyHaiDau) TongDoanhSoKyHaiDau,
                   SUM(ct.TongDoanhSoThucChay) TongDoanhSoThucChay,
                   ct.DmNhanHangREF,
                   ct.TenNhanHang,
                   ct.NgayThucHien
            FROM   RptNhanHangThongTinChiTiet ct
            WHERE  CONVERT(date, ct.NgayThucHien) = @NgayThucHien
            GROUP BY
                   ct.DmNhanHangREF,
                   ct.TenNhanHang,ct.NgayThucHien
	   )rptc  ON  dnh.DmNhanHangID = rptc.DmNhanHangREF
	          

	--SELECT '1'
END

--EXEC [Rpt_InsertNhanHangThongTinChiTiet] '2013-01-01'

```
