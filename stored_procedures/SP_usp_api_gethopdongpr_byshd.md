# Stored Procedure: `usp_api_gethopdongpr_byshd`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-12-05 14:32:32.533000
- **Ngày sửa cuối**: 2018-12-05 15:04:15.133000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@p_sohopdong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.usp_api_gethopdongpr_byshd
	-- Add the parameters for the stored procedure here
	@p_sohopdong NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT DISTINCT
	HopDongID,
	SoHopDong,
	NgayDanhSo,
	tensale,
	TenKhachHang,
	ISNULL(tonggiatri,0) tonggiatri,
	ISNULL(tientreo,0) tientreo,
	ISNULL(tonggiatri,0) - ISNULL(tientreo,0) tienconlai,
	codau
	FROM
	(
	SELECT 
	A.HopDongID,
	A.SoHopDong,
	CONVERT(NVARCHAR(10),NgayDanhSoHopDong,103) AS NgayDanhSo,
	B.HoVaTen tensale,
	ISNULL(C.TenPhongBan,'') + '->' + ISNULL(D.TenBoPhan,'') + '->' + ISNULL(E.TenNhom,'') AS phongban,
	F.TenKhachHang ,
	(SELECT SUM(hdct.ThanhTien) FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongFK = A.HopDongID AND hdct.DeletedStatus = 0 AND hdct.DmSanPhamREF IN (141,637)) tonggiatri,
	( SELECT SUM(tt.GiaTien) FROM dbo.ThucChayHopDongChiTietPR AS tt WHERE tt.HopDongREF = A.HopDongID ) AS tientreo,
	CASE WHEN ISNULL(A.NgayChuyenHopDongChoKeToan,'1900-01-01') > '1900-01-01' OR ISNULL(A.NgayNhanHopDongBanCung,'1900-01-01') > '1900-01-01' THEN 1 ELSE 0 END codau
	FROM dbo.HopDong A LEFT JOIN dbo.NhanSuSoYeuLyLich B ON A.SysNhanVienREF = B.NhanSuSoYeuLyLichID
	LEFT JOIN dbo.DmPhongBan C ON A.DmPhongBanREF = C.DmPhongBanID
	LEFT JOIN dbo.DmBoPhan D ON A.DmBoPhanREF = D.DmBoPhanID
	LEFT JOIN dbo.DmNhom E ON A.DmNhomREF = E.DmNhomID
	LEFT JOIN dbo.KhachHangThongTinChung F ON A.DmKhachHangREF = F.KhachHangThongTinChungID
	WHERE  A.TrangThaiHopDong NOT IN (0,3)
			AND A.SoHopDong = @p_sohopdong
	) KQ

	SELECT 
	     Z.phanboid 
		,Z.hd_id
		,Z.nhanhang
		,Z.website_id
		,Z.tenwebsite
		,Z.soluong
		,Z.donvitinh
		,Z.donviid
		,Z.dongia
		,Z.chietkhau
		,iskhuyenmai
		,ISNULL(Z.thanhtientruocck,0) AS thanhtientruocck
		,ISNULL(Z.tientreo, 0) AS tientreo
		,ISNULL(Z.thanhtientruocck,0) - ISNULL(Z.tientreo,0) AS chenhlech
		, Z.SoHopDongHT
	FROM
	(
	SELECT 
				 A.HopDongChiTietID AS phanboid
				,E.HopDongID hd_id
				,A.NhanHang
				,D.DmWebsiteID website_id
				,D.TenWebsite
				,A.SoLuong
				,C.TenDonViTinh donvitinh
				,C.DmDonViTinhID donviid
				,A.DonGia
				,A.ChietKhau
				,A.IsKhuyenMai
				,A.SoLuong * A.DonGia thanhtientruocck
				,(SELECT SUM(GiaTien) FROM ThucChayHopDongChiTietPR tc WHERE tc.DeletedStatus = 0 AND tc.HopDongChiTietREF = A.HopDongChiTietID) tientreo
				,A.SoHopDongHT
	FROM dbo.HopDongChiTiet A INNER JOIN dbo.DmSanPham B ON A.DmSanPhamREF = B.DmSanPhamID
	INNER JOIN dbo.DmDonViTinh C ON A.DonViTinhREF = C.DmDonViTinhID
	INNER JOIN dbo.DmWebsite D ON A.DmWebsiteREF = D.DmWebsiteID
	INNER JOIN dbo.HopDong E ON A.HopDongFK = E.HopDongID
	WHERE E.SoHopDong = @p_sohopdong
	AND E.TrangThaiHopDong NOT IN (0,3)
	AND A.DeletedStatus = 0
	AND A.DmSanPhamREF IN (141,637)
	) Z
END

```
