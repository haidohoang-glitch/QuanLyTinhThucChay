# Function: `ThucChay_GetListContractForDuyetDuLieu`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:06.447000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FilterString` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION dbo.ThucChay_GetListContractForDuyetDuLieu
(	
	-- Add the parameters for the function here
	@FilterString nvarchar(2000)
)
RETURNS  
@ThucChay TABLE (
	[ThucChayDaTinhID] [nvarchar](50) NOT NULL,
	[SoHopDong] [nvarchar](50) NULL,
	[HopDongChiTietREF] [int] NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](255) NULL,
	[SoLuongTheoHopDong] [bigint] NULL,
	[DonViTinh] [nvarchar](50) NULL,
	[DotChayHopDong] [nvarchar](2000) NULL,
	[TenWebsite] [nvarchar](255) NULL,
	[DmWebsiteREF] int null,
	[DonGia] [int] NULL,
	[ChietKhau] [int] NULL,
	[ThanhTienSauChietKhau] [float] NULL,
	[SoLuongThucChayKM] [bigint] NOT NULL,
	[SoLuongThucChay] [bigint] NULL,
	[ThanhTienThucThu] [float] NULL
	)
AS
BEGIN
	DECLARE @Sql nvarchar(4000)
	DECLARE @DauNhay nvarchar(50)
	
	SET @DauNhay = ''''
	
	SET @Sql = '
	SELECT
		A.ThucChayDaTinhID,
		A.SoHopDong, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
		(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
		A.DonViTinh,A.DotChayHopDong, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
		A.ThanhTien AS ThanhTienSauChietKhau,
		A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
		(SoLuongThucChayNoiBo+SoLuongThucChayThucThu) AS SoLuongThucChay,
		(ThanhTienThucChayNoiBo + ThanhTienThucThu) AS ThanhTienThucThu
	FROM
	(
		SELECT
			MAX(0) AS ThucChayDaTinhID,
			SoHopDong,HopDongChiTietREF,DmSanPhamREF,TenSanPham,TenWebsite,DmWebsiteREF, 
			dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
			DotChayHopDong,
			ChietKhau,DonGia,ThanhTien,
			CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongHopDongNoiBo,
			CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongHopDongKhuyenMai,
			CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongHopDongThucThu,
			CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongThucChayNoiBo,
			ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
			CASE WHEN UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongThucChayThucThu,
			CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
				ELSE 0
			END AS ThanhTienThucChayNoiBo,
			ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
			ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
			CASE WHEN UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
				ELSE 0
			END AS ThanhTienThucThu
		FROM ThucChayDaTinh
		WHERE IsPheDuyet = 0 AND TrangThaiHopDong <> 3 ' + @FilterString + '
		GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),TenMaHopDong,ThanhTienKM,
			DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien
	)A
	WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
					OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 
	'
	
	INSERT INTO @ThucChay (
							[ThucChayDaTinhID],
							[SoHopDong],
							[HopDongChiTietREF],
							[DmSanPhamREF],
							[TenSanPham],
							[SoLuongTheoHopDong],
							[DonViTinh],
							[DotChayHopDong],
							[TenWebsite],
							[DmWebsiteREF],
							[DonGia],
							[ChietKhau],
							[ThanhTienSauChietKhau],
							[SoLuongThucChayKM],
							[SoLuongThucChay],
							[ThanhTienThucThu]
							)
	SELECT
						A.ThucChayDaTinhID,
						A.SoHopDong, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
						(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
						A.DonViTinh,A.DotChayHopDong, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
						A.ThanhTien AS ThanhTienSauChietKhau,
						A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
						(SoLuongThucChayNoiBo+SoLuongThucChayThucThu) AS SoLuongThucChay,
						(ThanhTienThucChayNoiBo + ThanhTienThucThu) AS ThanhTienThucThu
					FROM
					(
						SELECT
							MAX(0) AS ThucChayDaTinhID,
							SoHopDong,HopDongChiTietREF,DmSanPhamREF,TenSanPham,TenWebsite,DmWebsiteREF, 
							dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
							DotChayHopDong,
							ChietKhau,DonGia,ThanhTien,
							CASE WHEN UPPER(TenMaHopDong) LIKE 'NB%' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
								ELSE 0
							END AS SoLuongHopDongNoiBo,
							CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
								ELSE 0
							END AS SoLuongHopDongKhuyenMai,
							CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE 'NB%') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
								ELSE 0
							END AS SoLuongHopDongThucThu,
							CASE WHEN UPPER(TenMaHopDong) LIKE 'NB%' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
								ELSE 0
							END AS SoLuongThucChayNoiBo,
							ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
							CASE WHEN UPPER(TenMaHopDong) NOT LIKE 'NB%' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
								ELSE 0
							END AS SoLuongThucChayThucThu,
							CASE WHEN UPPER(TenMaHopDong) LIKE 'NB%' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
								ELSE 0
							END AS ThanhTienThucChayNoiBo,
							ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
							ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
							CASE WHEN UPPER(TenMaHopDong) NOT LIKE 'NB%' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
								ELSE 0
							END AS ThanhTienThucThu
						FROM ThucChayDaTinh
						WHERE IsPheDuyet = 0 AND TrangThaiHopDong <> 3  and CONVERT(DATE,NgayThucHien) Between 'Sep  1 2013 12:00AM' and 'Sep 15 2013 12:00AM' and DmSanPhamREF in (339) and (TenDangNhap = 'quynhvtn' OR (DmWebsiteREF in (13,85,177,182)))
						GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),TenMaHopDong,ThanhTienKM,
							DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien
					)A
					WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
									OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0
	
	RETURN
END

```
