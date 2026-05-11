# Stored Procedure: `usp_NhanHang_SelectDmByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:46.807000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(1000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectDmByID]
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
		   [TenNhaPhanPhoi] =  STUFF(
			   (
					SELECT ';' + npp.TenKhachHang
					FROM   KhachHangThongTinChung AS npp
					WHERE  npp.KhachHangThongTinChungID IN (SELECT * FROM  dbo.Split(DmNhanHang.DmNhaPhanPhoiREF, ',') )
						FOR XML PATH(''), TYPE
				).value('.','NVARCHAR(MAX)'),1,1,''
			),
	       DmNhanHang.DmKhachhangSohuuREF,
	       (
	           SELECT TenChuSoHuu
	           FROM   DmChuSoHuuNhanhang
	           WHERE  DmChuSoHuuID = DmKhachhangSohuuREF
	       ) AS TenKhachhangSohuu,
		   DmNhanHang.TinhTrangGiayPhep,
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
