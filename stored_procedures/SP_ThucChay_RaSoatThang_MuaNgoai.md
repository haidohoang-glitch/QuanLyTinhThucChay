# Stored Procedure: `ThucChay_RaSoatThang_MuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-12-26 15:46:10.280000
- **Ngày sửa cuối**: 2022-12-26 15:47:10.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Tungay` | `date(3)` | No |
| `@Denngay` | `date(3)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<phuongvtt>
-- Create date: <2022-12-26>
-- Description:	<Xuat thuc chay theo khoang thoi gian - Ra Soat thang>
-- =============================================
CREATE PROCEDURE ThucChay_RaSoatThang_MuaNgoai
	-- Add the parameters for the stored procedure here
	@Tungay date
	, @Denngay date
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- tttcTong đang chưa đúng	
	SELECT
		A.HopDongID,
		 A.SoHopDong,
		 B.NhanHang,
		 B.HoVaTen,
		 B.Email,
		 A.HopDongChiTietREF,
		 A.TenHinhThucQuangCao,
		 A.TenSanPham,
		 B.ThanhTienHD,
		 SUM(A.tttcThang) Thucchay,
		 SUM(A.tttcTong) ThucChayTong 
	FROM
		(
			SELECT HopDongID,	SoHopDong, hdct.NhanHang, e.FULL_NAME AS HoVaTen
				, e.EMAIL_OFFICIAL Email
				, hdct.DmLoaiREF, hdct.TenLoai,  DmSanPhamREF,TenSanPham,hdct.HopDongChiTietID, 
				(CASE WHEN trangthaihopdong = 3 THEN 0 ELSE SUM(hdct.ThanhTien)END) ThanhTienHD
			FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK		
							LEFT JOIN ASDAG2.HRM.dbo.EMPLOYEES e ON ID = hd.SysNhanVienREF 				
	WHERE 1=1 
	AND (hdct.DmLoaiREF IN (13) OR hdct.DmLoaiBannerREF = 18)
	GROUP BY hd.SoHopDong, hd.HopDongID, hd.TrangThaiHopDong, e.FULL_NAME,e.EMAIL_OFFICIAL,hdct.DmLoaiREF, hdct.TenLoai,  DmSanPhamREF,TenSanPham, hdct.HopDongChiTietID, hdct.NhanHang
	)B
	RIGHT JOIN 
	(SELECT X.*, Y.tttcTong FROM 
	(SELECT tcdt.HopDongID,
		tcdt.SoHopDong,
		tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,
		tcdt.TenHinhThucQuangCao,
		tcdt.DmSanPhamREF ,
		tcdt.TenSanPham,
		ROUND(ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) tttcThang
		FROM  dbo.ThucChayDaTinh tcdt
	WHERE tcdt.NgayThucHien BETWEEN @tungay AND @denngay
	AND (tcdt.DmHinhThucQuangCao=13 OR tcdt.DmLoaiBannerREF=18)
	GROUP BY tcdt.HopDongChiTietREF,
		  tcdt.HopDongID,
		  tcdt.SoHopDong,
		tcdt.DmHinhThucQuangCao,
		tcdt.TenHinhThucQuangCao,
		tcdt.DmSanPhamREF ,
		tcdt.TenSanPham
	) X
	INNER JOIN
	(
	SELECT tcdt.HopDongID,
		tcdt.SoHopDong,
		tcdt.HopDongChiTietREF,
		ROUND(ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) tttcTong
		FROM  dbo.ThucChayDaTinh tcdt
	WHERE 1=1 
	AND (tcdt.DmHinhThucQuangCao=13 OR tcdt.DmLoaiBannerREF=18)
	GROUP BY tcdt.HopDongChiTietREF,
		  tcdt.HopDongID,
		  tcdt.SoHopDong
	) Y
	ON X.HopDongID = Y.HopDongID AND X.HopDongChiTietREF=Y.HopDongChiTietREF 
	)A
	ON B.HopDongID=A.HopDongID AND B.HopDongChiTietID=A.HopDongChiTietREF AND B.TenSanPham=A.TenSanPham
	GROUP BY 
		A.HopDongID,
		A.SoHopDong,
		B.HoVaTen,
		--B.MaNhanSu,
		B.Email,
		A.HopDongChiTietREF,
		 A.TenHinhThucQuangCao,
		 A.TenSanPham,
		 B.ThanhTienHD
		 , B.NhanHang
		 HAVING  SUM(A.tttcThang) <>0
		 ORDER BY A.HopDongID DESC




	
END

```
