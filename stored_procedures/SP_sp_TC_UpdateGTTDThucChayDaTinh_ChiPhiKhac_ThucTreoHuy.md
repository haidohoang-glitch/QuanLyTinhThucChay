# Stored Procedure: `sp_TC_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:23:12.637000
- **Ngày sửa cuối**: 2022-07-06 16:22:17.287000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[sp_TC_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy]  '2018-12-04', 'QC0221018'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy]
    @NgayThucHien DATETIME,
	@pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @HopDongID INT ,
            @HopDongChiTietID INT ,
            @DmNhanHangREF NVARCHAR(50) ,
            @SoLuong INT ,
            @DonGia INT,
			@ThucChayHopDongChiTietID INT
        DECLARE @NgayGioiHanTinh DATETIME ,
			@NgayDanhSoGioiHan DATETIME = '2021-10-01',
			@NgayDanhSoGioiHan_Tiktok DATETIME = '2022-01-01',
            @GiaTriThayDoi BIGINT = 0 ,
            @SoLuongThayDoi BIGINT = 0 ,
            @ChietKhau INT ,
            @Count_TCDT INT = 0,
			@ThanhTienThucTreo FLOAT
        SET @NgayGioiHanTinh = '2013-01-01'

        DECLARE Cursor_chiphikhac CURSOR
        FOR
            SELECT  C.HopDongFK ,
                    C.HopDongChiTietID ,
                    tchdt.DmNhanHangREF ,
                    tchdt.SoLuongThucTreo ,
                    tchdt.ThanhTienThucTreo,
					tchdt.ThucChayHopDongChiTietID
            FROM    ( SELECT    hdct.HopDongFK , hdct.HopDongChiTietID , hdct.DmSanPhamREF , hdct.DmLoaiREF , hdct.DmLoaiBannerREF ,hdct.DmViTriREF,
                                hdct.DmWebsiteREF , hdct.SoLuong , hdct.DonGia , hdct.ChietKhau , hdct.ThanhTien
                      FROM      dbo.HopDongChiTiet hdct
						WHERE 1=1 AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 		
						AND hdct.DeletedStatus = 0
                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
						--AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMANTIC
                    ) C
                    INNER JOIN ( SELECT *
                                 FROM   dbo.HopDong hd
                                 WHERE  hd.TrangThaiHopDong <> 3
                                        AND hd.DeletedStatus = 0
										AND (@pSoHopDong IS NULL OR	hd.SoHopDong = @pSoHopDong)
                               ) D ON D.HopDongID = C.HopDongFK
                    INNER JOIN ( SELECT DmNhanHangREF ,HopDongChiTietREF ,HopDongREF ,SoLuongThucTreo SoLuongThucTreo,
										ThanhTien AS ThanhTienThucTreo, ThucChayHopDongChiTietID
                                 FROM   dbo.ThucChayHopDongChiTiet
                                 WHERE  DeletedStatus = 1
                                        AND CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                               ) tchdt ON C.HopDongChiTietID = tchdt.HopDongChiTietREF
            WHERE   1 = 1
            AND tchdt.SoLuongThucTreo > 0
            AND C.DmWebsiteREF NOT IN ( 307, 285 ) -- loai tru website Google, Facebook
			AND NOT (C.DmSanPhamREF = 5184 AND D.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
			AND NOT ((C.DmSanPhamREF = 5188  OR C.DmViTriREF = 100774) AND  (D.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --haidh comment 20211026 TikTok tinh theo pp GGFB
	
        OPEN Cursor_chiphikhac
        FETCH NEXT FROM Cursor_chiphikhac INTO @HopDongID, @HopDongChiTietID,
            @DmNhanHangREF, @SoLuong, @ThanhTienThucTreo, @ThucChayHopDongChiTietID
        WHILE @@FETCH_STATUS = 0
            BEGIN
                SET @Count_TCDT = (
										SELECT COUNT(tc.HopDongChiTietREF) FROM
										 ( SELECT  HopDongID, HopDongChiTietREF, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ThanhTienThucChay
										, SUM(ThanhTienKM + GiaTriKMThayDoi)ThanhTienKM
										FROM    dbo.ThucChayDaTinh
										WHERE   HopDongChiTietREF = @HopDongChiTietID
										AND DotChayBooking = convert(nvarchar(100),@ThucChayHopDongChiTietID)
										AND NgayThucHien <= @NgayThucHien
										GROUP BY  HopDongID, HopDongChiTietREF
									  )tc
									  WHERE tc.ThanhTienThucChay <> 0 OR tc.ThanhTienKM <> 0
								 )

			--Tinh gia tri thay doi
                IF ( @Count_TCDT > 0 )
                    BEGIN
                        SET @GiaTriThayDoi = @ThanhTienThucTreo
                        SET @GiaTriThayDoi = (-1) * ISNULL(@GiaTriThayDoi, 0)
						--tinh so luong thay doi
                        SET @SoLuongThayDoi = (-1) * ISNULL(@SoLuong, 0)
                        PRINT 'tinh gia tri thay doi'
                        EXEC [dbo].[sp_TC_InsertGTTDThucChayDaTinh_ChiPhiKhac] @NgayThucHien,
                            @HopDongChiTietID, @DmNhanHangREF, @GiaTriThayDoi,
                            @SoLuongThayDoi , @ThucChayHopDongChiTietID


                    END
                SET @GiaTriThayDoi = 0
                SET @SoLuongThayDoi = 0
                FETCH NEXT FROM Cursor_chiphikhac INTO @HopDongID,
                    @HopDongChiTietID, @DmNhanHangREF, @SoLuong, @ThanhTienThucTreo, @ThucChayHopDongChiTietID
            END
    CLOSE Cursor_chiphikhac
    DEALLOCATE Cursor_chiphikhac

	--Tính thực chạy chi phi theo số hợp đồng vào ngày thực hiện của toàn bộ các thực treo chưa được tính (recordstatus = 0)
	EXEC [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_ByHopDong]
		   @NgayThucHien = @NgayThucHien
		  , @pSoHopDong = @pSoHopDong
		
END


```
