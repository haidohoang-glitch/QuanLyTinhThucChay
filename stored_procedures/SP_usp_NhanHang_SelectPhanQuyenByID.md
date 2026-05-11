# Stored Procedure: `usp_NhanHang_SelectPhanQuyenByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-29 14:19:06.417000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.057000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectPhanQuyenByID]
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
