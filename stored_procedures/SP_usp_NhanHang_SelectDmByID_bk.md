# Stored Procedure: `usp_NhanHang_SelectDmByID_bk`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:57.337000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(1000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectDmByID_bk]
	@DmNhanHangID VARCHAR(1000)
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	DECLARE @Result NVARCHAR(MAX);
	
	SET @Result = @DmNhanHangID;
	
	SELECT [DmNhanHangID],
	       [TenNhanHang],
	       [MucDoNhan],
	       [DmNghanhHangREF],
	       TenChienDich AS DmChienDichREF,
	       [TenChienDichNhan] = STUFF(
	           (
	               SELECT ';' + B.TenChienDich
	               FROM   DmChienDichNhanhang AS B
	               WHERE  B.DmChienDichID IN (SELECT *
	                                          FROM   dbo.Split(DmNhanHang.TenChienDich, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       [NhanSuSoYeuLyLichREF],
	       [DmNhanHangThayDoiID],
	       [TenNghanhHang] = STUFF(
	           (
	               SELECT ';' + md.TenNghanhHang
	               FROM   DmNghanhHang md
	               WHERE  md.DeletedStatus <> 1
	                      AND md.DmNghanhHangID IN (SELECT *
	                                                FROM   dbo.Split(DmNhanHang.DmNghanhHangREF, ','))
	                          FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       DmNhanHang.NhanHangCha,
	       (
	           SELECT A.TenNhanHang
	           FROM   DmNhanHang AS A
	           WHERE  A.DmNhanHangID = DmNhanHang.NhanHangCha
	       ) AS TenNhanCha,
	       DmNhanHang.DmNhaPhanPhoiREF,
	       [TenNhaPhanPhoi] = STUFF(
	           (
	               SELECT ';' + npp.TenKhachHang
	               FROM   KhachHangFull AS npp
	               WHERE  npp.KhachHangID IN (SELECT *
	                                          FROM   dbo.Split(DmNhanHang.DmNhaPhanPhoiREF, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       (
	           SELECT shn.TenKhachHang
	           FROM   KhachHangFull AS shn
	           WHERE  shn.KhachHangID = DmKhachhangSohuuREF
	       ) KhachhangSohuu,
	       '' AS TenNhanSu,
	       DmNhanHang.DmKhachhangSohuuREF,
	       (
	           SELECT shn.TenKhachHang
	           FROM   KhachHangFull AS shn
	           WHERE  shn.KhachHangID = DmKhachhangSohuuREF
	       ) AS TenKhachhangSohuu,
	       DmNhanHang.Ghichu,
	       DmNhanHang.[CreatedBy],
	       DmNhanHang.[CreatedAt],
	       DmNhanHang.[LastModidfiedBy],
	       DmNhanHang.[LastModifiedAt],
	       DmNhanHang.[DeletedStatus],
	       DmNhanHang.[PrintStatus],
	       DmNhanHang.[RecordStatus]
	FROM   [dbo].[DmNhanHang] AS DmNhanHang
	WHERE  [DmNhanHangID] IN (SELECT *
	                          FROM   dbo.[Split](@Result, ','))
	       AND DmNhanHang.DeletedStatus <> 1
END

```
