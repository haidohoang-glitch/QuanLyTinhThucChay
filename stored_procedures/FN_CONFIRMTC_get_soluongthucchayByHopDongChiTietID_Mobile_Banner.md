# Function: `CONFIRMTC_get_soluongthucchayByHopDongChiTietID_Mobile_Banner`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-03-20 17:43:59.843000
- **Ngày sửa cuối**: 2017-03-20 18:19:53.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@ThongTinThucChayMobileSponsor` | `nvarchar` | No |
| `@ThongTinThucChayCPM` | `nvarchar` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[CONFIRMTC_get_soluongthucchayByHopDongChiTietID_Mobile_Banner] 
(
		@HopDongChiTietID INT,
        @DmSanPhamREF INT,
        @DonViTinhREF INT,
        @ThongTinThucChayMobileSponsor NVARCHAR(MAX),
        @ThongTinThucChayCPM NVARCHAR(MAX),
        @NgayThucHien DATETIME,
        @FromDate DATETIME,
        @ToDate DATETIME)
RETURNS BIGINT
BEGIN
	DECLARE @v_SoLuongThucChay INT,@v_SLTC_NgayBatDau INT, @v_SLTC_NgayKetThuc INT
			, @v_SLHDCT INT, @v_countbanner INT, @HopDongID INT, @v_loaiBanner INT, @ChietKhau INT; 
	DECLARE @v_PhanBoChinhID INT, @v_SoLuongPhanBo INT, @v_isphanbochinh int;
    DECLARE @v_bannerID nvarchar(200);
    
    set @v_PhanBoChinhID = 0;
    set @v_isphanbochinh = 0;
    set @HopDongID = 0;
    set @v_countbanner = 0;
    set @v_bannerID = '';
    set @v_SoLuongThucChay = 0;
    set @v_SoLuongPhanBo = 0;
    set @v_PhanBoChinhID  =0;
    set @v_loaiBanner  = 0;
    /*
    (	-- NHOM SP CPD
	    --140 --Banner CPD
        --,228 -- Boxapp CPD
        --,564 --Boxapp MultiBand
        --,549 --CPD Chuyen trang
    	
    ) 
    */

	--IF(pDmSanPhamREF IN(140,228,564,549))THEN
 --   	select pb.`loai_banner_id` into @v_loaiBanner 
 --       FROM `hdcn_phanbosite` pb
 --       where pb.`id` = pPhanBoID;
        
 --       IF(@v_loaiBanner = 5)THEN
 --       	BEGIN
 --           	IF(pFromDate = '1900-01-01' AND pToDate = '1900-01-01') THEN
 --               	 SELECT  SUM(IFNULL(
 --                       ( DATEDIFF(A.`thoigianketthuc` , A.`thoigianbatdau`) +1 )
 --                     ,0)) into @v_SoLuongThucChay
 --                     FROM
 --                     (
 --                       SELECT DISTINCT pb.`hd_id`, pb.`id`, tc.`thoigianbatdau`
 --                       , IF(tc.`thoigianketthuc` > NgayThucHien, NgayThucHien,tc.`thoigianketthuc`) AS thoigianketthuc
 --                       FROM `hdcn_phanbosite` pb
 --                       INNER JOIN `hdcn_thucchay` tc ON pb.`id` = tc.`phanbosite_id`
 --                       WHERE 1=1
 --                       AND pb.`loaihinh_id` = pDmSanPhamREF
 --                       AND pb.id = pPhanBoID
 --                       AND tc.`thoigianbatdau` <= NgayThucHien
 --                     )A GROUP by A.hd_id, A.id;
 --               ELSE
 --                     SELECT  SUM(IFNULL(
 --                       ( DATEDIFF(A.`thoigianketthuc` , A.`thoigianbatdau`) +1 )
 --                     ,0)) into @v_SoLuongThucChay
 --                     FROM
 --                     (
 --                       SELECT DISTINCT pb.`hd_id`, pb.`id`
 --                       , IF(tc.`thoigianbatdau` < pFromDate, pFromDate,tc.`thoigianbatdau`) AS thoigianbatdau
	--		            , IF(tc.`thoigianketthuc` > pToDate, pToDate,tc.`thoigianketthuc`) AS thoigianketthuc
 --                       FROM `hdcn_phanbosite` pb
 --                       INNER JOIN `hdcn_thucchay` tc ON pb.`id` = tc.`phanbosite_id`
 --                       WHERE 1=1
 --                       AND pb.`loaihinh_id` = pDmSanPhamREF
 --                       AND pb.id = pPhanBoID
 --                       AND NOT (tc.`thoigianbatdau` > pToDate OR tc.`thoigianketthuc` < pFromDate)
 --                     )A GROUP by A.hd_id, A.id;   
 --               END IF;
             
 --           END;  
 --        ELSE
 --              BEGIN
 --              		IF(pFromDate = '1900-01-01' AND pToDate = '1900-01-01') THEN
 --                       SELECT  SUM(IFNULL(
 --                         ( DATEDIFF(A.`thoigianketthuc` , A.`thoigianbatdau`) +1 )
 --                       ,0)) into @v_SoLuongThucChay
 --                       FROM
 --                       (
 --                         SELECT DISTINCT pb.`hd_id`, pb.`id`, tc.`thoigianbatdau`, tc.`booking_id`
 --                         , IF(tc.`thoigianketthuc` > NgayThucHien, NgayThucHien,tc.`thoigianketthuc`) AS thoigianketthuc
 --                         FROM `hdcn_phanbosite` pb
 --                         INNER JOIN `hdcn_thucchay` tc ON pb.`id` = tc.`phanbosite_id`
 --                         WHERE 1=1
 --                         AND pb.`loaihinh_id` = pDmSanPhamREF
 --                         AND pb.id = pPhanBoID
 --                         AND tc.`thoigianbatdau` <= NgayThucHien
 --                       )A GROUP by A.hd_id, A.id;	
 --                   ELSE
 --                   	SELECT  SUM(IFNULL(
 --                         ( DATEDIFF(A.`thoigianketthuc` , A.`thoigianbatdau`) +1 )
 --                       ,0)) into @v_SoLuongThucChay
 --                       FROM
 --                       (
 --                         SELECT DISTINCT pb.`hd_id`, pb.`id`
 --                         , IF(tc.`thoigianbatdau` < pFromDate, pFromDate,tc.`thoigianbatdau`) AS thoigianbatdau
 --                         , tc.`booking_id`
 --                         , IF(tc.`thoigianketthuc` > pToDate, pToDate,tc.`thoigianketthuc`) AS thoigianketthuc
 --                         FROM `hdcn_phanbosite` pb
 --                         INNER JOIN `hdcn_thucchay` tc ON pb.`id` = tc.`phanbosite_id`
 --                         WHERE 1=1
 --                         AND pb.`loaihinh_id` = pDmSanPhamREF
 --                         AND pb.id = pPhanBoID
 --                         AND NOT (tc.`thoigianbatdau` > pToDate OR tc.`thoigianketthuc` < pFromDate)
 --                       )A GROUP by A.hd_id, A.id;	
 --                   END IF;
 --              END;     
 --        END IF;#
 --    END IF;  #END NHOM SP CPD
 --     /*
 --   	--- NHOM SP TMDT --------------
 --       -- Tin vip	241
 --       -- Box nÃ¡Â»â€¢i bÃ¡ÂºÂ­t	264
 --       -- Box sÃ¡ÂºÂ£n phÃ¡ÂºÂ©m Hot	300
 --       -- SiÃƒÂªu chÃ„Æ’m sÃƒÂ³c	268
 --       -- Tin vip xuyÃƒÂªn trang	248
 --       -- sÃƒÂ n BÃ„ÂS	270
 --       -- Tin nÃ¡Â»â€¢i bÃ¡ÂºÂ­t	243
 --       -- Top giao dÃ¡Â»â€¹ch hot 244
 --       -- Tin Ã„â€˜ÃƒÂ­nh 249
 --    */
 --    IF(pDmSanPhamREF IN (241,264,300,268,248,270,243,244,249,385))THEN
 --    	IF (pDonViTinhREF in (3,4,5,6))THEN
 --       BEGIN
 --       	IF(pFromDate = '1900-01-01' AND pToDate = '1900-01-01') THEN
 --                 SELECT  SUM(IFNULL(
 --                   ( DATEDIFF(A.`thoigianketthuc` , A.`thoigianbatdau`) +1 )
 --                 ,0)) into @v_SoLuongThucChay
 --                 FROM
 --                 (
 --                   SELECT pb.`hd_id`, pb.`id`, tc.`thoigianbatdau`
 --                   , IF(tc.`thoigianketthuc` > NgayThucHien, NgayThucHien,tc.`thoigianketthuc`) AS thoigianketthuc
 --                   FROM `hdcn_phanbosite` pb
 --                   INNER JOIN `hdcn_thucchay` tc ON pb.`id` = tc.`phanbosite_id`
 --                   WHERE 1=1
 --                   AND pb.`loaihinh_id` = pDmSanPhamREF
 --                   AND pb.id = pPhanBoID
 --                   AND tc.`thoigianbatdau` <= NgayThucHien
 --                 )A GROUP by A.hd_id, A.id;
 --           ELSE
 --                 SELECT  SUM(IFNULL(
 --                   ( DATEDIFF(A.`thoigianketthuc` , A.`thoigianbatdau`) +1 )
 --                 ,0)) into @v_SoLuongThucChay
 --                 FROM
 --                 (
 --                   SELECT pb.`hd_id`, pb.`id`
 --                   , IF(tc.`thoigianbatdau` < pFromDate, pFromDate,tc.`thoigianbatdau`) AS thoigianbatdau
	--	            , IF(tc.`thoigianketthuc` > pToDate, pToDate,tc.`thoigianketthuc`) AS thoigianketthuc
 --                   FROM `hdcn_phanbosite` pb
 --                   INNER JOIN `hdcn_thucchay` tc ON pb.`id` = tc.`phanbosite_id`
 --                   WHERE 1=1
 --                   AND pb.`loaihinh_id` = pDmSanPhamREF
 --                   AND pb.id = pPhanBoID
 --                   AND NOT (tc.`thoigianbatdau` > pToDate OR tc.`thoigianketthuc` < pFromDate)
 --                 )A GROUP by A.hd_id, A.id;
 --           END IF; 
 --        END; 
 --        ELSE
 --        	SELECT count(tc.`phanbosite_id`) into @v_SoLuongThucChay
 --           FROM `hdcn_thucchay` tc
 --           WHERE tc.`phanbosite_id` = pPhanBoID ;
 --        END IF; 
 --    END IF; #END NHOM SP TMDT
 --    /*---------CHI PHI-------------
 --        242 -- Luot up												
 --        --- NHOM SP Chi phiÃŒÂ--
 --       , 251 --ThiÃ¡ÂºÂ¿t kÃ¡ÂºÂ¿, quÃ¡ÂºÂ£n lÃƒÂ½
 --       , 252 --Hosting
 --       , 253 --Chi phi khac									
 --       , 535 --Chi phÃƒÂ­ quÃ¡ÂºÂ£n lÃƒÂ½ campaign
 --       , 537 --Chi phÃƒÂ­ viÃ¡ÂºÂ¿t bÃƒÂ i
 --       , 538 --Chi phÃƒÂ­ thiÃ¡ÂºÂ¿t kÃ¡ÂºÂ¿
 --       , 539 --Chi phÃƒÂ­ dÃ¡Â»Â±ng clip
 --       , 540 --Chi phÃƒÂ­ sÃƒÂ¡ng tÃ¡ÂºÂ¡o
 --       , 541 --Chi phÃƒÂ­ giÃ¡ÂºÂ£i thÃ†Â°Ã¡Â»Å¸ng cuÃ¡Â»â„¢c thi/ Contest
 --       , 542 --Chi phÃƒÂ­ xÃƒÂ¢y dÃ†Â°ng microsite/ tab
 --       , 555 --Chi phiÃŒÂ traÃŒâ‚¬i trÃ†Â¡ÃŒÂ£
 --       , 556 --HiÃƒÂªÃŒÂ£u Ã„â€˜iÃŒÂnh
 --       , 557 --CheÃŒâ‚¬n Clip
 --       , 558 --Chi phiÃŒÂ viÃƒÂªÃŒÂt baÃŒâ‚¬i
 --       , 559 --Chi phiÃŒÂ quay clip
 --       , 560 --Chi phÃƒÂ­ sÃ¡ÂºÂ£n xuÃ¡ÂºÂ¥t										
 --       , 561 -- Chi phÃƒÂ­ khÃ¡ÂºÂ£o sÃƒÂ¡t thÃ¡Â»â€¹ trÃ†Â°Ã¡Â»Âng online
 --   */
 --   IF(pDmSanPhamREF IN (242,251,252, 253, 535, 537, 538 , 539 , 540, 541, 542 , 555 , 556, 557, 558, 559, 560, 561))THEN
 --   	SELECT count(tc.`phanbosite_id`) into @v_SoLuongThucChay
 --       FROM `hdcn_thucchay` tc
 --       WHERE tc.`phanbosite_id` = pPhanBoID ;
 --   END IF;  #END CHI PHI    
 --   /*
 --   --CAC SAN PHAM PR
 --   --141	Ã„ÂÃ„Æ’ng tin
 --   --245	BÃ¡ÂºÂ£o trÃ¡Â»Â£ thÃƒÂ´ng tin
 --   --250	Giao lÃ†Â°u trÃ¡Â»Â±c tuyÃ¡ÂºÂ¿n
 --   */
 --    IF(pDmSanPhamREF in (141,245,250))THEN
 --    	SELECT count(pr.`phanbosite_id`) into @v_SoLuongThucChay
 --       FROM `hdcn_thucchay_pr` pr
 --       WHERE pr.`phanbosite_id` = pPhanBoID;
 --    END IF;#END CAC SAN PHAM PR
 --    /*--CAC SAN PHAM CPM(BALLOON, BOXAPP CPM, TVC, STICK, KINGSIZE)*/
 --    IF((pDmSanPhamREF IN (339,240,370,598,613)))THEN
 --    	IF(pFromDate = '1900-01-01' AND pToDate = '1900-01-01') THEN
 --        SELECT 
 --               SUM( DISTINCT
 --                   IF(pDonViTinhREF = 1
 --                     ,tc.`TongViewThucChay` * b.`TiLeBanner`
 --                     ,tc.`TongClickThucChay`* b.`TiLeBanner`
 --                     )/100
 --                 )  
 --                 INTO @v_SoLuongThucChay
 --             FROM `ThucChayCPMChot` tc
 --             INNER JOIN `BannerThucTreo`  b
 --             ON tc.`DmBannerID` = b.`DmBannerID`
 --             AND b.`PhanBoSite_id` = pPhanBoID;
 --        ELSE
 --            BEGIN
	--							#@v_SLTC_NgayBatDau, @v_SLTC_NgayKetThuc
 --               SET @v_SLTC_NgayBatDau = 0;
 --               SET @v_SLTC_NgayKetThuc = 0;
	--							#XAC DINH SLTC NGAYBATDAU->pFromDate
 --                  SELECT 
 --                   SUM( DISTINCT
 --                       IF(pDonViTinhREF = 1
 --                         ,tc.`TongViewThucChay` * b.`TiLeBanner`
 --                         ,tc.`TongClickThucChay`* b.`TiLeBanner`
 --                         )/100
 --                     )
 --                     INTO @v_SLTC_NgayBatDau
 --                 FROM `ThucChayCPMChotNgay` tc
 --                 INNER JOIN `BannerThucTreo`  b
 --                 ON tc.`DmBannerID` = b.`DmBannerID`
 --                 AND b.`PhanBoSite_id` = pPhanBoID
 --                 WHERE tc.NgayThucHien < pFromDate;	 
 --            	#XAC DINH SLTC NGAYBATDAU->pToDate
 --                  SELECT 
 --                    SUM( DISTINCT
 --                       IF(pDonViTinhREF = 1
 --                         ,tc.`TongViewThucChay` * b.`TiLeBanner`
 --                         ,tc.`TongClickThucChay`* b.`TiLeBanner`
 --                         )/100
 --                     )
 --                     INTO @v_SLTC_NgayKetThuc
 --                 FROM `ThucChayCPMChotNgay` tc
 --                 INNER JOIN `BannerThucTreo`  b
 --                 ON tc.`DmBannerID` = b.`DmBannerID`
 --                 AND b.`PhanBoSite_id` = pPhanBoID
 --                 WHERE tc.NgayThucHien <= pToDate;	 
	--							SET @v_SLTC_NgayBatDau = IFNULL(@v_SLTC_NgayBatDau,0);
	--							SET @v_SLTC_NgayKetThuc = IFNULL(@v_SLTC_NgayKetThuc,0);
 --               #XAC DINH SLHD
 --               #1-CPM; 2-CPC
 --                 SELECT IF(PB.`thoigian_unit` = 1,PB.`thoigian_val`*1000,PB.`thoigian_val`)
 --                 	INTO @v_SLHDCT
 --                 FROM `hdcn_phanbosite` PB
 --                 WHERE PB.`id` = pPhanBoID
 --                 AND PB.`thoigian_unit` IN (1,2);
	--								SET @v_SLHDCT = IFNULL(@v_SLHDCT,0);

 --                 IF(@v_SLTC_NgayBatDau > @v_SLHDCT)THEN #NEU SLTC->NGAYBATDAU > SLHD
 --                 	SET @v_SoLuongThucChay = 0;
 --                 ELSE
 --                 	IF( @v_SLTC_NgayKetThuc <= @v_SLHDCT)THEN
 --                   	SET @v_SoLuongThucChay = @v_SLTC_NgayKetThuc - @v_SLTC_NgayBatDau;
 --                   ELSE #@v_SLTC_NgayKetThuc > @v_SLHDCT
 --                   BEGIN
 --                   	SET @v_SoLuongThucChay = @v_SLHDCT - @v_SLTC_NgayBatDau;
 --                       #LECH TREO HA = @v_SLTC_NgayKetThuc - @v_SLHDCT
 --                   END;    
 --                   END IF;
 --                 END IF;
 --            END;
 --        END IF; 
 --         SET @v_SoLuongThucChay = IFNULL(@v_SoLuongThucChay,0);
 --    END IF;#END CAC SAN PHAM CPM
 --    /*--CAC SAN PHAM MOBILE VA SPONSOR*/
 --    IF((pDmSanPhamREF IN (342,381)))THEN
	--			IF(pFromDate = '1900-01-01' AND pToDate = '1900-01-01') THEN
	--			BEGIN
	--					SELECT SUM(SoLuongThucChayThucThu) INTO @v_SoLuongThucChay
	--					FROM BannerThucTreoPhanBoMobile
	--					WHERE PhanBoSite_id = pPhanBoID;
	--			END;#END CHECK pFromDate = '1900-01-01' AND pToDate = '1900-01-01'
	--			ELSE
	--			BEGIN
	--					#@v_SLTC_NgayBatDau, @v_SLTC_NgayKetThuc
	--					SET @v_SLTC_NgayBatDau = 0;
	--					SET @v_SLTC_NgayKetThuc = 0;
	--					#XAC DINH SLTC NGAYBATDAU->pFromDate, #XAC DINH SLTC NGAYBATDAU->pToDate, 	#XAC DINH SLHD
	--					SELECT SUM(SLTC_DenNgayBDCF), SUM(SLTC_DenNgayKTCF),SoLuong  INTO @v_SLTC_NgayBatDau, @v_SLTC_NgayKetThuc, @v_SLHDCT
	--					FROM BannerThucTreoPhanBoMobile
	--					WHERE PhanBoSite_id = pPhanBoID
	--					GROUP BY SoLuong;
						
	--					SET @v_SLTC_NgayBatDau = IFNULL(@v_SLTC_NgayBatDau,0);
	--					SET @v_SLTC_NgayKetThuc = IFNULL(@v_SLTC_NgayKetThuc,0);

	--					#1-CPM; 2-CPC
	--					IF(@v_SLTC_NgayBatDau > @v_SLHDCT)THEN #NEU SLTC->NGAYBATDAU > SLHD
	--						SET @v_SoLuongThucChay = 0;
	--					ELSE
	--						IF( @v_SLTC_NgayKetThuc <= @v_SLHDCT)THEN
	--							SET @v_SoLuongThucChay = @v_SLTC_NgayKetThuc - @v_SLTC_NgayBatDau;
	--						ELSE #@v_SLTC_NgayKetThuc > @v_SLHDCT
	--						BEGIN
	--							SET @v_SoLuongThucChay = @v_SLHDCT - @v_SLTC_NgayBatDau;
	--								#LECH TREO HA = @v_SLTC_NgayKetThuc - @v_SLHDCT
	--						END;    
	--						END IF;
	--					END IF;
	--			END;#END CHECK VOI CONFIRM THUC CHAY THEO NGAY
	--			END IF;	# (pFromDate = '1900-01-01' AND pToDate = '1900-01-01') VOI NHOM MOBILE
 --    END IF;#END CAC SAN PHAM MOBILE VA SPONSOR
  SET @v_SoLuongThucChay = ISNULL(@v_SoLuongThucChay,0)
  RETURN @v_SoLuongThucChay
END
```
