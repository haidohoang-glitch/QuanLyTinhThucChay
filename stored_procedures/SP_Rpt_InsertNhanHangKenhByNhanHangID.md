# Stored Procedure: `Rpt_InsertNhanHangKenhByNhanHangID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:27.513000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.650000

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

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangKenhByNhanHangID] 
	@DmNhanHangID INT
AS
BEGIN
	
	--delete data RptNhanHangHinhThucKy
	DELETE FROM rptNhanHangKenh
	WHERE DmNhanHangREF = @DmNhanHangID
	 
	--insert data RptNhanHangHinhThucKy
	INSERT INTO RptNhanHangKenh
	  (
	    -- RptNhanHangKenhID -- this column value is auto-generated
	    DmNhanHangREF,
	    TenNhanHang,
	    DmNganhHangREF,
	    TenNganhHang,
	    DmKenhREF,
	    TenKenh,
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
	       '' tennganhhang,
	       rnhttct.DmKenhREF,
	       rnhttct.TenKenh,
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
	WHERE  rnhttct.DmNhanHangREF = @DmNhanHangID
	GROUP BY
	       rnhttct.DmNhanHangREF,
	       rnhttct.TenNhanHang,
	       rnhttct.DmKenhREF,
	       rnhttct.TenKenh,
	       rnhttct.NgayThucHien
	--SELECT '1'
END

--EXEC [Rpt_InsertNhanHangKenh] '2013-01-01'

```
