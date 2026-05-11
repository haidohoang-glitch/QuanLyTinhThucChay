# Stored Procedure: `InsertFromThucChayHopDongChiTietToThuChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 19:02:00.387000
- **Ngày sửa cuối**: 2014-10-14 10:39:58.610000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE InsertFromThucChayHopDongChiTietToThuChay
	-- Add the parameters for the stored procedure here

AS
BEGIN
INSERT INTO dbo.ThucChay
	SELECT 
	NEWID(),
	B.SoHopDong,
	'',
	c.DmSanPhamREF,
	C.TenSanPham,
	C.DmNhomWebsiteREF,
	C.TenNhomWebsite,
	C.DmWebsiteREF,
	C.TenWebsite,
	'',
	'',
	A.DmBannerREF,
	A.TenBanner,
	A.ThoiGianBatDau,
	0,--TongView
	0,--TongClick
	A.CreatedBy,
	A.CreatedAt,
	A.LastModifiedBy,
	A.LastModifiedAt,
	0,
	0,
	0,
	0,--TongSoBaiViet
	A.HopDongChiTietREF

	FROM 
	dbo.ThucChayHopDongChiTiet A
	INNER JOIN dbo.HopDong B ON A.HopDongREF = B.HopDongID
	INNER JOIN dbo.HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
END

```
