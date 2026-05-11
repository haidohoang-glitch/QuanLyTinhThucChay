# Stored Procedure: `sp_KSTC_Admatic_BrandProtectionPage_ChayChuaTreo_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-09-25 15:11:30.080000
- **Ngày sửa cuối**: 2023-09-25 15:38:51.427000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_Admatic_BrandProtectionPage_ChayChuaTreo_V2]
-- Add the parameters for the stored procedure here
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    --- Check các banner admatic đã chạy sản phẩm BrandProtectionPage nhưng chưa treo

    ---List hợp đồng BrandProtectionPage đơn vị <> URL
    DECLARE @Table_programmatic TABLE
    (
        Sohopdong NVARCHAR(50),
        hopdongchitiet INT,
		DmSanPhamREF INT,
		DonViTinhRef INT,
        thanhtien FLOAT       
    );
    INSERT INTO @Table_programmatic
    (
        Sohopdong,
        hopdongchitiet,
		DmSanPhamREF,
		DonViTinhRef,
        thanhtien     
    )
    SELECT h.SoHopDong,
           hdct.HopDongChiTietID,
		   hdct.DmSanPhamREF,
		   hdct.DonViTinhREF,
           hdct.ThanhTien           
    FROM dbo.HopDong h
	INNER JOIN dbo.HopDongChiTiet hdct ON h.HopDongID = hdct.HopDongFK    
    WHERE hdct.DmLoaiREF = 42 
			AND hdct.DmSanPhamREF = 5312 AND hdct.DonViTinhREF <> 84      
          AND hdct.DeletedStatus = 0

    ---select *from @Table_programmatic

    SELECT DISTINCT
           A.SoHopDong,
           A.NhanHopDong,
           A.DmBannerREF,
           A.DmSanPhamREF,
           A.TenSanPham,
           B.*
    FROM
    (
        SELECT tc.SoHopDong,
               hd.NhanHopDong,
               CONVERT(NVARCHAR(50), DmBannerREF) DmBannerREF,
               DmSanPhamREF,
               TenSanPham
        FROM dbo.ThucChay tc
            LEFT JOIN HopDong hd
                ON tc.SoHopDong = hd.SoHopDong
        WHERE 1 = 1
              AND NgayThucHien >= '2021-01-01'
              AND tc.CreatedBy = 'From API_Admatic'
              --and DmBannerREF ='564083'	 
              AND tc.SoHopDong NOT IN ( 'hd_demo', '', 'HD DEMO', 'hd_king_test2', 'HD SELFSERVE', 'TEST', 'HD TEST',
                                        'DEMO', 'HD PROG'
                                      )
              AND tc.SoHopDong NOT LIKE '%demo%'
              AND tc.SoHopDong NOT LIKE '%test%'
              AND tc.SoHopDong NOT IN ( 'NB0340523', 'NB0350523', 'NB0180623', 'NB0190623', 'NB0200623', 'NB0250623',
                                        'NB0300723', 'NB0310723', 'NB0330523', 'NB0160623', 'NB0280723', 'NB0220723'
                                      ) --list hđ Programtic theo mail: Về vấn đề ghi nhận thực chạy cho các hợp đồng Admicro x Xaxis
			-----Chỉ check SAN PHAM BRAND PROTECT 
			AND tc.DmSanPhamREF = 5312
        UNION ALL
        SELECT tc.SoHopDong,
               hd.NhanHopDong,
               DmBannerID DmBannerREF,
               DmSanPhamREF,
               TenSanPham
        FROM dbo.ThucChay_ThanhTien_Admatic tc
            LEFT JOIN HopDong hd
                ON tc.SoHopDong = hd.SoHopDong
        WHERE 1 = 1
              AND NgayThucHien >= '2021-01-01'
              AND tc.SoHopDong NOT IN ( 'hd_demo', '', 'HD DEMO', 'hd_king_test2', 'HD SELFSERVE', 'TEST', 'HD TEST',
                                        'DEMO', 'HD PROG'
                                      )
              AND tc.SoHopDong NOT LIKE '%demo%'
              AND tc.SoHopDong NOT LIKE '%test%'
              AND tc.SoHopDong NOT IN ( 'NB0340523', 'NB0350523', 'NB0180623', 'NB0190623', 'NB0200623', 'NB0250623',
                                        'NB0300723', 'NB0310723', 'NB0330523', 'NB0160623', 'NB0280723', 'NB0220723'
                                      ) --list hđ Programtic theo mail: Về vấn đề ghi nhận thực chạy cho các hợp đồng Admicro x Xaxis
			-----Chỉ check SAN PHAM BRAND PROTECT 
			AND tc.DmSanPhamREF = 5312
    ) A
        FULL OUTER JOIN
        ---Check treo lấy về ASD thucchay
        --(select distinct convert(nvarchar(50),DmBannerREF)DmBannerREF
        --from Thucchayhopdongchitiet where 
        --1=1 
        --and  DmHinhThucQuangCaoREF = 42 
        --and DeletedStatus = 0 and HopDongChiTietREF not in (0,-1)
        ----check treo trên nguồn
        (
            SELECT DISTINCT
                   CONVERT(NVARCHAR(50), Banner_Id) DmBannerREF
				   --, Contract_detail_id
            FROM [ASDAG2].ThucTreo.dbo.ThucTreo
            WHERE 1 = 1
                  AND Product_Formality_Id = 42
                  --AND Deleted_Status = 0 --Duongnt commnent: các dòng treo sau đó xóa đi có nguyên nhân thay đổi cách tính nên vẫn tính có treo
                  AND Contract_Detail_Id NOT IN ( 0, -1 )

		----check treo Đích + bổ sung loại đơn vị Bài, URL --Duongnt comment
		--(select distinct convert(nvarchar(50),t.DmBannerREF)DmBannerREF  from Thucchayhopdongchitiet t
		--INNER JOIN dbo.HopDongChiTiet c ON c.HopDongChiTietID = t.HopDongChiTietREF
		--WHERE      1=1 
  --      and  t.DmHinhThucQuangCaoREF = 42 
  --      and t.DeletedStatus = 0 and t.HopDongChiTietREF not in (0,-1)
		--AND NOT ( c.DmSanPhamREF = 5312 AND c.DonViTinhREF = 84)
		--AND NOT ( c.DmSanPhamREF = 598 AND c.DonViTinhREF = 7)

        ) B
            ON A.DmBannerREF = B.DmBannerREF
			--haidh commnet sua lai dieu kien check progammatic 20230925
			--WHERE  NOT EXISTS(SELECT TOP (1) hopdongchitiet  FROM @Table_programmatic t WHERE t.HopDongChitiet = B.Contract_Detail_id )
    WHERE A.SoHopDong IN
          (
              SELECT Sohopdong FROM @Table_programmatic
          )
          AND B.DmBannerREF IS NULL
          AND A.DmBannerREF NOT IN ( 80778 ) -- admatic confirm hủy treo


    ----and A.DmBannerREF not in (79603, 79581,80237,80125,80236,80124,80026,80490,80491 ) -- chạy program matic
    ORDER BY A.SoHopDong;



END;




```
