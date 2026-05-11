# Stored Procedure: `usp_PhanQuyenNhanHang_Select_ByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:13:21.927000
- **Ngày sửa cuối**: 2014-10-14 16:52:08.430000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_PhanQuyenNhanHang_Select_ByID]
	@DmPhanQuyenID INT
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	SELECT [DmPhanQuyenID],
	       [DmNhanHangREF],
	       [OxUserREF],
	       [NhanSuREF],
	       [TenNhanSu],
	       [MaNhanSu],
	       [TenPhongBan],
	       [TenBoPhan],
	       [TenNhom],
	       [ThoiGianHieuLuc],
	       [ThoiGianHetHieuLuc],
	       [KichHoat],
	       [CreatedBy],
	       [CreatedAt],
	       [LastModifiedBy],
	       [LastModifiedAt]	       
	FROM   [dbo].[PhanQuyenNhanHang]
	WHERE  [DmPhanQuyenID] = @DmPhanQuyenID
END

```
