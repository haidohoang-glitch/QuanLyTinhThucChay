# Stored Procedure: `ThucChay_MuaNgoai_CheckDuToanBan_Mua`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-12-27 09:46:08.333000
- **Ngày sửa cuối**: 2023-12-05 15:38:33.780000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<phuongvtt>
-- Create date: <2022-12-26>
-- Description:	<check du toan ban < du toan mua>
-- =============================================
CREATE PROCEDURE ThucChay_MuaNgoai_CheckDuToanBan_Mua
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT A.*, B.SoLuongMua, DonGiaMua, B.ChietKhauMua,B.DuToanMua, B.ThucChayMua , A.DuToanBan - B.DuToanMua AS ChenhLechBan_Mua
	FROM (
		SELECT SoHopDong,hopdongfk HopDongID, HopDongChiTietID,hdct.DmSanPhamREF,hdct.TenSanPham,hdct.TenWebsite,hdct.TenViTri,hdct.SoLuong, hdct.DonGia, hdct.DonViTinh,hdct.ChietKhau
		,ThanhTien DuToanBan, hd.LastModifiedAt AS NgaySua_HD
		FROM hopdongchitiet hdct inner join hopdong hd on hopdongid = hopdongfk
		WHERE hdct.DeletedStatus <>1 -- 1 là xóa
			AND (DmLoaiREF = 13 or DmLoaiBannerREF =18)
			AND nam>=2018 and TrangThaiHopDong <> 3
	)A
	LEFT JOIN 
	(
		select HopDongChiTietID,SoLuongMua, DonGiaMua,  ChietKhauMua, ThanhTienSauCKMua DuToanMua, SUM(tcm.ThanhTienMuaNgoaiTruocCK) AS ThucChayMua
		from dbo.HopDongChiTiet_MuaNgoai m INNER JOIN dbo.ThucChayMuaNgoaiChiTiet tcm ON HopDongChiTietID = tcm.HopDongChiTietREF  
		WHERE m.DeletedStatus = 0 AND tcm.DeletedStatus = 0
		GROUP BY HopDongChiTietID,SoLuongMua, DonGiaMua,  ChietKhauMua, ThanhTienSauCKMua
		HAVING SUM(tcm.ThanhTienMuaNgoaiTruocCK) <> 0
	)B
	ON A.HopDongChiTietID = B.HopDongChiTietID
	where A.DuToanBan < B.DuToanMua AND A.HopDongChiTietID NOT IN (SELECT HopDongChiTietREF FROM dbo.HopDong_MuaNgoai_Lo)
	AND A.HopDongChiTietID NOT IN (694733,694734,683364,683365,683366)-- A Ngọc đã cf bán lỗ, ASD xử lý để các tháng k xuất lại check nhiều lần nhé
	order by A.HopDongID DESC, A.HopDongChiTietID
	END

```
