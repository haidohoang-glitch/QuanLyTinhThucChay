# Stored Procedure: `usp_NhanHang_SelectByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:27:25.150000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectByID]
	@DmNhanHangID INT
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	SELECT dnh.DmNhanHangID,
	       dnh.TenNhanHang,
	       dnh.NhanHangCha,
	       dnh.MucDoNhan,
	       dnh.TenChienDich,
	       dnh.DmNghanhHangREF,
	       dnh.NhanSuSoYeuLyLichREF,
	       dnh.DmNhanHangThayDoiID,
	       dnh.DmKhachhangKyREF,
	       dnh.DmKhachhangSohuuREF,
	       dnh.DmNhaPhanPhoiREF,
	       dnh.HopdongChitietREF,
	       dnh.TinhTrangGiayPhep,
	       dnh.Ghichu,
	       dnh.CreatedBy,
	       dnh.CreatedAt,
	       dnh.LastModidfiedBy,
	       dnh.LastModifiedAt,
	       dnh.DeletedStatus,
	       dnh.PrintStatus,
	       dnh.RecordStatus,
	       dnh.FromSystem,
	       dnh.LastLogTime,
	       dnh.LastLogSystem
	FROM   DmNhanHang dnh
	WHERE  dnh.DmNhanHangID = @DmNhanHangID
	       AND dnh.DeletedStatus <> 1
END

```
