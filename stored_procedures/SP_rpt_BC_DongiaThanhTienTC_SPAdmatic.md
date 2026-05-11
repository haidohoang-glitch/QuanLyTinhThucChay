# Stored Procedure: `rpt_BC_DongiaThanhTienTC_SPAdmatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-04-18 09:46:24.890000
- **Ngày sửa cuối**: 2023-04-18 10:02:21.327000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@TotalRows` | `int(4)` | Yes |

## Definition (Source Code)

```sql

/*
	DECLARE @TotalRows INT;
EXEC [dbo].[rpt_BC_DongiaThanhTienTC_SPAdmatic] @SoHopDong = N'QC3960223',           -- nvarchar(100)
													@PhanBoID=0,
                                                  @PageIndex = 1,                -- int
                                                  @PageSize = 10000,                 -- int
                                                  @TotalRows = @TotalRows OUTPUT -- int

*/

CREATE PROCEDURE [dbo].[rpt_BC_DongiaThanhTienTC_SPAdmatic]
--DECLARE
    @SoHopDong NVARCHAR(100) ='',
	@PhanBoID int =NULL,
    @PageIndex INT=1,
    @PageSize INT=2000000,
    @TotalRows INT OUT
AS
BEGIN

DECLARE @HopDongID INT;
SELECT @HopDongID = HopdongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong

  DECLARE @FromIndex INT,
            @ToIndex INT,
            @SQL NVARCHAR(MAX),
            @Fillter NVARCHAR(MAX);

	SET @Fillter = N'1=1';
    SET @FromIndex = (@PageIndex - 1) * @PageSize + 1;
    SET @ToIndex = (@PageIndex * @PageSize);


---Thông tin thực chạy
SELECT A.*,
       B.SoLuong_TCDT,
       B.ThanhTien_TCDT
INTO #KQ
FROM
(
    SELECT hdct.HopDongFK, tt.HopDongChiTietREF,
		hdct.DmLoaiREF, hdct.TenLoai,hdct.TenSanPham SanPham_PB,hdct.DmSanPhamREF, hdct.SoLuong Soluong_PB,hdct.DonViTinh DonVi_PB,hdct.DonGia DonGia_PB,hdct.ChietKhau ChietKhau_PB,dbo.FormatNumber(hdct.ThanhTien) ThanhTien_PB,
           tt.DmBannerREF,           
           tc.TenSanPham [SP_GhiNhan],
           dbo.FormatNumber(SUM(tc.SoLuongThucChay)) Số_lượng,
           dbo.FormatNumber(SUM(tc.ThanhTienThucChaySauCK_ChuaVAT)) ThanhTien_SauCK_ChuaVAT,
           MIN(tc.NgayThucHien) NgayBD_SP,
           MAX(tc.NgayThucHien) NgayKT_SP,
           ROUND((SUM(tc.ThanhTienThucChaySauCK_ChuaVAT) / SUM(tc.SoLuongThucChay)), 3) Đơn_giá_SP
    FROM dbo.ThucChay_ThanhTien_Admatic tc
        INNER JOIN dbo.ThucChayHopDongChiTiet tt  ON tc.DmBannerID = tt.DmBannerREF
		INNER JOIN dbo.HopDongChiTiet hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID AND hdct.DeletedStatus = 0
    GROUP BY hdct.HopDongFK, tt.HopDongChiTietREF,
	hdct.DmLoaiREF, hdct.TenLoai, hdct.TenSanPham,hdct.DmSanPhamREF, hdct.SoLuong,hdct.DonViTinh ,hdct.DonGia ,hdct.ChietKhau ,hdct.ThanhTien,
             tt.DmBannerREF,
             tc.TenSanPham
             --tc.TenWebsite
) A
    INNER JOIN
    (
        SELECT DmBannerREF,				
               dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi)) SoLuong_TCDT,
               dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) ThanhTien_TCDT
        FROM dbo.ThucChayDaTinh
        GROUP BY DmBannerREF
    ) B
        ON A.DmBannerREF = B.DmBannerREF
WHERE  A.HopDongFK = @HopDongID 
	AND ( ISNULL(@PhanBoID,0) = 0 or A.HopDongChiTietREF =  @PhanBoID )
	AND A.DmLoaiREF = 42
    AND A.DmSanPhamREF NOT IN ( 817, 140, 549 )
ORDER BY A.HopDongChiTietREF;

DECLARE @SQL_TotalRows NVARCHAR(MAX), @SQL_TotalRowPara NVARCHAR(MAX), @v_TotalRow FLOAT;

		SET @SQL = N'SELECT * FROM (SELECT ROW_NUMBER() OVER ( ORDER BY A.HopDongChiTietREF ) AS STT,'+ @SoHopDong +' * FROM #KQ A  WHERE ' + @Fillter + N') B WHERE STT BETWEEN '
			+ CONVERT(NVARCHAR(10), @FromIndex) + N' AND ' + CONVERT(NVARCHAR(10), @ToIndex) + N' ORDER BY b.HopDongChiTietREF' + N'';

			--SELECT * FROM (SELECT ROW_NUMBER() OVER ( ORDER BY A.HopDongChiTietREF ) AS STT, * FROM #KQ A  WHERE 1=1) B WHERE STT BETWEEN 1 AND 10000 ORDER BY b.TenHinhThucQuangCao

	PRINT @SQL;
	EXECUTE (@SQL);



	SET @SQL_TotalRowPara = N'@v_TotalRow bigint output ';
	SET @SQL_TotalRows = N'SELECT @v_TotalRow=  
     COUNT(*) FROM   
    #KQ A WHERE ' + @Fillter + N'';

	EXECUTE sp_executesql @SQL_TotalRows, @SQL_TotalRowPara, @v_TotalRow = @TotalRows OUTPUT;

END

```
