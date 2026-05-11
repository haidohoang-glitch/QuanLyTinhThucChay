# Stored Procedure: `usp_Nhansu_SearchNhansuByName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:49.560000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.803000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhansu` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhansu_SearchNhansuByName]
	@TenNhansu NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT TOP 20
	       A.SalerID AS OxUserID,
	       B.NhanSuSoYeuLyLichID AS NhanSuID,
	       B.MaNhanSu,
	       B.HoVaTen,
	       B.Email,
	       G.TenChucDanh,
	       D.TenPhongBan,
	       E.TenBoPhan,
	       F.TenNhom
	FROM   AdminPermisionHDCN AS A
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
	WHERE  B.HoVaTen COLLATE SQL_Latin1_General_CP1_CI_AI LIKE '%' + @TenNhansu  + '%'
	       AND B.DeletedStatus <> 1
	       AND B.NgayNghiViec IS NULL
	       AND C.[Active] = 1
END

```
