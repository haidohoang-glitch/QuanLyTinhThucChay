# Stored Procedure: `HopDongPRTreoVuot`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-16 16:39:27.800000
- **Ngày sửa cuối**: 2019-05-16 16:58:47.167000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE HopDongPRTreoVuot 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	select A.HopDongREF, A.SoHopDong,A.TenSanPham,A.ThucTreo, B.SoHopDong,B.TenSanPham,B.ThanhTien,
	 isnull(A.ThucTreo,0) - isnull(B.ThanhTien,0) TreoVuot
	 from (
	SELECT HopDongREF,dbo.GetSoHopDongByID(HopDongREF) SoHopDong,DmSanPhamREF,
	isnull(TenSanPham,N'Treo không có sản phẩm')TenSanPham,
	round(sum(SoLuong*GiaTien*(100-ChietKhau)/100),0)ThucTreo
	from ThucChayHopDongChiTietPR a
	left join DmSanPham b on A.DmSanPhamREF = b.DmSanPhamID
	where a.DeletedStatus = 0 and RIGHT(dbo.GetSoHopDongByID(HopDongREF),2)>='18'
	group by  HopDongREF,DmSanPhamREF,TenSanPham
	having sum(SoLuong*GiaTien*(100-ChietKhau)/100) <> 0
	)A
	left join

	(select HopDongID, SoHopDong,DmSanPhamREF,TenSanPham, sum(hdct.ThanhTien)ThanhTien from HOpDong hd 
	inner join HopDongChiTiet hdct on HopDongID = HopDongFK
	where DmSanPhamREF in (141,305,637) and not (DmLoaiBannerREF =18 or DmLoaiREF = 13)
	and TrangThaiHopDong <> 3 and hdct.DeletedStatus =0
	group by  HopDongID, SoHopDong,DmSanPhamREF,TenSanPham
	)B
	on A.HopDongREF = B.HopDongID
	and A.DmSanPhamREF = B.DmSanPhamREF
	where isnull(A.ThucTreo,0) - isnull(B.ThanhTien,0) > 100
END

```
