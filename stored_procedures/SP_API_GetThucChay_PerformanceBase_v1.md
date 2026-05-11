# Stored Procedure: `API_GetThucChay_PerformanceBase_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-12 16:12:54.680000
- **Ngày sửa cuối**: 2021-04-12 16:12:54.680000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--select * from ThucChay_PerformanceBase_ThayDoi
--API_GetThucChay_PerformanceBase N'QC5760320'
create PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_v1]
    -- Add the parameters for the stored procedure here
    @SoHopDong NVARCHAR(50)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    DECLARE @HopDongID INT;
	

    SELECT @HopDongID = HopDongID FROM HopDong WHERE SoHopDong = @SoHopDong
	
    -- Insert statements for procedure here
    SELECT 
           @SoHopDong SoHopDong,
           HopDongID,
           phanBoId HopDongChiTietREF,
           DmSanPhamREF,
           TenSanPham,
           TK_Admarket,
           thanhTienPhanBoVAT ThanhTien,
           DmViTriREF,
           TenViTri,
           thucChayTongVAT TienThucChayTong,
           thucChayVAT TienThucChay,
           ThucChayDenNgay	
    FROM
    (
        SELECT A.*,
               B.DmViTriREF viTriId,
               B.TenViTri tenViTri,
               B.ThucChayVAT thucChayVAT,
               B.ThucChayDenNgay thucChayDenNgay
			   --,B.Username,
			   --B.TenNhanVien
        FROM
        (
            SELECT HopDongFK hopDongId,
                   HopDongChiTietID phanBoId,
                   DmSanPhamREF sanPhamId,
                   TenSanPham tenSanPham,
                   TK_AdMarket taiKhoan,
                   ThanhTien*1.1 thanhTienPhanBoVAT 
            FROM dbo.HopDongChiTiet
            WHERE HopDongFK = @HopDongID
                  AND DmSanPhamREF IN ( 144, 585, 628 )
                  AND DmLoaiREF <> 42
        ) A LEFT JOIN (
                SELECT HopDongChiTietREF,
                       DmViTriREF,
                       (CASE
                            WHEN DmViTriREF = 1 THEN
                                'AdX'
                            WHEN DmViTriREF = 2 THEN
                                'AdX Mobile'
                            WHEN DmViTriREF = 3 THEN
                                'AdX Ecommerce'
                            WHEN DmViTriREF = 0 THEN
                                ''
                            ELSE
                                ''
                        END
                       )  TenViTri,
					   --TenDangNhap AS Username,
					   --TenNhanVien AS TenNhanVien,
                       round(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)*1.1,0) ThucChayVAT,
                       MAX(NgayThucHien) ThucChayDenNgay
                FROM ThucChayDaTinhAdmarket
                WHERE TrangThaiHopDong <> 3
                      AND DmHinhThucQuangCao <> 42
                GROUP BY HopDongChiTietREF,
                         DmViTriREF,
                         TenViTri, TenDangNhap,TenNhanVien
            ) B ON A.phanBoId = B.HopDongChiTietREF
    ) TCacc
        LEFT JOIN
        (
            SELECT hdct.TK_AdMarket,
                   hdct.DmSanPhamREF,
                   tc.DmViTriREF,
                   ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)*1.1, 0) ThucChayTongVAT
            FROM ThucChayDaTinhAdmarket tc
                INNER JOIN HopDongChiTiet hdct
                    ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
            WHERE 1 = 1
                  AND TK_AdMarket IN
                      (
                          SELECT DISTINCT
                                 TK_AdMarket
                          FROM HopDongChiTiet
                          WHERE HopDongFK = @HopDongID
                                AND DeletedStatus = 0
                                AND DmSanPhamREF IN ( 144, 628, 585 )
                                AND DmLoaiREF <> 42
                      )
                  AND TrangThaiHopDong <> 3
                  AND DmHinhThucQuangCao <> 42
            GROUP BY hdct.TK_AdMarket,
                     tc.DmViTriREF,
                     hdct.DmSanPhamREF
        ) TCTong
            ON TCacc.taiKhoan = TCTong.TK_AdMarket
               AND TCacc.sanPhamId = TCTong.DmSanPhamREF
               AND TCacc.viTriId = TCTong.DmViTriREF;

			
--	Id phân bổ

--- Sản phẩm: Tên sản phẩm + Tên vị trí (với sản phẩm AdX, DmViTriREF: 1.AdX Pc, 2.AdX Mobile,  3. AdX Ecommerce, sản phẩm khác AdX, không có Tên vị trí, DmViTriREF = 0)

--- Tài khoản (username)

--- Tiền thực chạy (chưa VAT)

--- Thực chạy đến ngày: max ngày thực hiện của phân bổ
	
END;





```
