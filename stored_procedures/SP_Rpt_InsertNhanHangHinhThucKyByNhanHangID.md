# Stored Procedure: `Rpt_InsertNhanHangHinhThucKyByNhanHangID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:27.257000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.300000

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

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangHinhThucKyByNhanHangID] 
	@DmNhanHangID INT
AS
BEGIN
	
	--delete data RptNhanHangHinhThucKy
	DELETE FROM RptNhanHangHinhThucKy
	WHERE DmNhanHangREF = @DmNhanHangID 
	 
	--insert data RptNhanHangHinhThucKy
	INSERT INTO RptNhanHangHinhThucKy
	  (
	    -- RptNhanHangHinhThucKyID -- this column value is auto-generated
	    DmNhanHangREF,
	    TenNhanHang,
	    DmNganhHangREF,
	    TenNganhHang,
	    HinhThucKyID,
	    HinhThucKy,
	    DoanhSoKyHaiDau,
	    DoanhSoThucChay,
	    TongDoanhSoHaiDau,
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
	       0 HinhThucKy,--Cho nay chua dien du lieu chinh xac
	       rnhttct.HinhThucKy, 
	       SUM(rnhttct.DoanhSoKyHaiDau)DoanhSoKyHaiDau,
	       SUM(rnhttct.DoanhSoThucChay)DoanhSoThucChay,
	       0 TongDoanhSoHaiDau,
	       rnhttct.NgayThucHien,
	       'ABM_nhan',
	       GETDATE(),
	       'ABM_nhan',
	       GETDATE(),
	       0,
	       0
	FROM   RptNhanHangThongTinChiTiet rnhttct
	WHERE  rnhttct.DmNhanHangREF = @DmNhanHangID
	GROUP BY
	       rnhttct.DmNhanHangREF,
	       rnhttct.TenNhanHang,
	       rnhttct.HinhThucKy,
	       rnhttct.NgayThucHien
	
	--SELECT '1'
END

--EXEC [Rpt_InsertNhanHangThongTinChiTiet] '2013-01-01'

```
