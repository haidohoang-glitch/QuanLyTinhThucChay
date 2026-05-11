# Stored Procedure: `Rpt_InsertNhanHangKhachHangKyByNhanHangID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:27.003000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.640000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangKhachHangKyByNhanHangID] 
	@DmNhanHangID INT
AS
BEGIN
	
	--delete data RptNhanHangHinhThucKy
	DELETE FROM RptNhanHangKhachHangKy
	WHERE DmNhanHangREF = @DmNhanHangID
	 
	--insert data RptNhanHangHinhThucKy
	INSERT INTO RptNhanHangKhachHangKy
	  (
	    -- RptNhanHangKhachHangKy -- this column value is auto-generated
	    DmNhanHangREF,
	    TenNhanHang,
	    DmNganhHangREF,
	    TenNganhHang,
	    DmKhachHangREF,
	    TenKhachHang,
	    DoanhSoKyHaiDau,
	    DoanhSoThucChay,
	    TongDoanhSoKyHaiDau,
	    NgayThucHien,
	    CreatedBy,
	    CreatedAt,
	    LastModifiedBy,
	    LastModifiedAt,
	    RecordStatus,
	    DeletedStatus
	  )
	SELECT rnhttct.DmNhanHangREF,
	       rnhttct.TenNhanHang,
	       '' DmNganhHangREF,
	       '' TenNganhHang,
	       rnhttct.DmKhachHangREF,
	       rnhttct.TenKhachHang,
	       SUM(rnhttct.DoanhSoKyHaiDau) DoanhSoKyHaiDau,
	       SUM(rnhttct.DoanhSoThucChay) DoanhSoThucChay,
	       0 TongDoanhSoKyHaiDau,
	       rnhttct.NgayThucHien,
	       'ABM_nhan',
	       GETDATE(),
	       'ABM_nhan',
	       GETDATE(),
	       0,
	       0
	FROM   RptNhanHangThongTinChiTiet rnhttct
	WHERE rnhttct.DmNhanHangREF = @DmNhanHangID
	GROUP BY
	       rnhttct.DmNhanHangREF,
	       rnhttct.TenNhanHang,
	       rnhttct.DmKhachHangREF,
	       rnhttct.TenKhachHang,
	       rnhttct.NgayThucHien
 
	--SELECT '1'
END

--EXEC [Rpt_InsertNhanHangKhachHangKy] '2013-01-01'

```
