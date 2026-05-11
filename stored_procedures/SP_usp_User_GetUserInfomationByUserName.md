# Stored Procedure: `usp_User_GetUserInfomationByUserName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-03-07 16:50:16.053000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserName` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_User_GetUserInfomationByUserName]
	@UserName NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT B.HoVaTen,
	       B.Email,
	       B.MaNhanSu,
	       G.TenChucDanh,
	       D.TenPhongBan,
	       E.TenBoPhan,
	       F.TenNhom
	FROM   dbo.AdminPermisionHDCN A
	       INNER JOIN dbo.NhanSuSoYeuLyLich B
	            ON  A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichID
	       INNER JOIN dbo.NhanSuQuaTrinhCongTac C
	            ON  C.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
	       LEFT JOIN dbo.DmPhongBan D
	            ON  C.DmPhongBanREF = D.DmPhongBanID
	       LEFT JOIN dbo.DmBoPhan E
	            ON  E.DmBoPhanID = C.DmBoPhanREF
	       LEFT JOIN dbo.DmNhom F
	            ON  F.DmNhomID = C.DmNhomLamViecREF
	       LEFT JOIN dbo.DmChucDanh G
	            ON  G.DmChucDanhID = C.DmChucDanhREF
	WHERE  UPPER(A.TenDangNhap) = UPPER(@UserName)
	       AND C.[Active] = 1
END

```
