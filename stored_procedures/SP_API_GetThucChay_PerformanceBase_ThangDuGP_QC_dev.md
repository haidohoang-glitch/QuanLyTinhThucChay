# Stored Procedure: `API_GetThucChay_PerformanceBase_ThangDuGP_QC_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-08-24 15:26:21.207000
- **Ngày sửa cuối**: 2025-06-27 15:19:39.860000

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
-- [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_QC] 'QC1810823'
--EXEC [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_QC_DEV]  @SoHopDong = N'QC2310525'
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_QC_dev] 
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50)
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @HopDongID INT;
	DECLARE @NgayThucHien2 datetime;
	DECLARE @NGAYBDKOAPDUNG_VAT DATETIME = '2022-03-29' --ngay ap dung vat
	, @NgayDanhSoGioiHan_MKT_FEE DATETIME = '2025-01-01'

    SELECT TOP (1) @HopDongID = HopDongID FROM HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID
	SELECT @NgayThucHien2 = convert(Date,dateadd(day,-1,getdate()))
	
	--1. LAY THONG TIN DU LIEU CUA CAC SAN PHAM CHAY TREN ADMARKET
	--------------------------------------------------0. Lay danh sach acc cua sohopdong truyen vao--------------------------------------------
	Declare @acc  table
	(
		username nvarchar(50),
		DmSanPhamREF int
	)
	Insert into @acc
	select distinct TK_AdMarket, DmSanPhamREF 
	from HopDongChiTiet hdct where HopDongFK = @HopDongID 					
					and DeletedStatus = 0 
					and DmSanPhamREF in (144,585,628)
					and DmLoaiREF <> 42

	--select * from @acc t where 1=1

--------------------------------------------------1. Lay thuc chay do team san pham tra ve cua acc------------------------------------------
	Declare @tcacc  table
	(
	username nvarchar(50),
	DmSanPhamREF int,
	DmViTriREF int,
	TienChinh_VAT float,
	TienChinh_BF_VAT FLOAT
	)
	Insert into @tcacc
	--thuc chay san pham ADX, VIEWPLUS, CPC ADMARKET	
	select tcdta1.username,  tcdta1.DmSanPhamREF,  tcdta1.DmViTriREF, tcdta1.TienChinh_Co_VAT  AS TienChinh_VAT, tcdta1.TienChinh_VAT AS TienChinh_BF_VAT
	FROM dbo.ThucChay_PerformanceBase_ViewAll tcdta1 
	WHERE 1=1 AND  exists (select 1 from @acc t where 1=1
					and t.DmSanPhamREF = tcdta1.DmSanPhamREF
					and t.username = tcdta1.username
					) 


	--SELECT A.username, A.DmSanPhamREF, A.DmViTriREF, A.TienChinh_VAT, B.TienChinh_BF_VAT FROM
	
	--(
	--select tcdta1.username,  tcdta1.DmSanPhamREF,  tcdta1.DmViTriREF, tcdta1.TienChinh_VAT, 0 AS TienChinh_BF_VAT
	--FROM dbo.[ThucChay_CPCAdmarket_ViewAll] tcdta1 
	--WHERE 1=1 AND  exists (select 1 from @acc t where 1=1
	--				and t.DmSanPhamREF = tcdta1.DmSanPhamREF
	--				and t.username = tcdta1.username
	--				) 
	--)A
	--INNER JOIN 
	--(
	--select tcdta1.username,  tcdta1.DmSanPhamREF,  tcdta1.DmViTriREF, 0 AS TienChinh_VAT, tcdta1.TienChinh_VAT AS TienChinh_BF_VAT
	--FROM dbo.[ThucChay_CPCAdmarket_ViewAll_BF_VAT] tcdta1 
	--WHERE 1=1 AND  exists (select 1 from @acc t where 1=1
	--				and t.DmSanPhamREF = tcdta1.DmSanPhamREF
	--				and t.username = tcdta1.username
	--				) 
	--)B ON A.username = B.username AND A.DmSanPhamREF = B.DmSanPhamREF AND A.DmViTriREF = B.DmViTriREF
	
	--select * from @tcacc
	-------------2. Lay thuc chay da ghi nhan tcdt cua acc
	declare @ngaythuchien nvarchar(50), @nth datetime
	select @ngaythuchien = CONVERT(VARCHAR(10),convert(date,getdate(),103),111) + ' 12:01:00'
	set @nth =  (select convert(datetime, @ngaythuchien))

	declare @tcdtacc table
	(
		username nvarchar(200),
		DmSanPhamREF int,
		DmViTriREF int,
		AllHopDongTongTCDT float
	)
	Insert into @tcdtacc
	select tc.TK_AdMarket,tc.DmSanPhamREF,isnull(tc.DmViTriREF,0) DmViTriREF, sum(AllHopDongTongTCDT) as AllHopDongTongTCDT 
	FROM (
				SELECT tcdt.TK_AdMarket,
									tcdt.DmSanPhamREF,
									tcdt.DmViTriREF,
									tcdt.TongTCDT AllHopDongTongTCDT
				FROM dbo.[ThucChayDaTinh_CPCAdmarket_ViewAll_BF_VAT_BF_VAT] tcdt
				where exists (select 1 from @acc where 1=1
						--and DmSanPhamREF = tcdta1.DmSanPhamREF
								and username = tcdt.TK_AdMarket
								) 

				union all
				-- lay du lieu truoc gio tinh
				select TK_Admarket, DmSanPhamREF, isnull(DmViTriREF,0) DmViTriREF,  SoTienThayDoi/1.08 AllHopDongTongTCDT
				FROM ThucChay_PerformanceBase_ThayDoi td
				where DeletedStatus = 0 and RecordStatus = 0 and LastModifiedAt < @nth
				and LastModifiedAt < @NGAYBDKOAPDUNG_VAT
				and exists (select 1 from @acc where 1=1 and username = td.TK_AdMarket ) 

				union all
				select TK_Admarket, DmSanPhamREF, isnull(DmViTriREF,0) DmViTriREF,  SoTienThayDoi AllHopDongTongTCDT 
				FROM ThucChay_PerformanceBase_ThayDoi td
				where DeletedStatus = 0 and RecordStatus = 0 and LastModifiedAt < @nth
				and LastModifiedAt >= @NGAYBDKOAPDUNG_VAT
				and exists (select 1 from @acc where 1=1 and username = td.TK_AdMarket ) 

				union all
				-- lay du lieu sau gio tinh
				select TK_Admarket, DmSanPhamREF, isnull(DmViTriREF,0) DmViTriREF,  SoTienThayDoi/1.08 AllHopDongTongTCDT
				from ThucChay_PerformanceBase_ThayDoi td
				where DeletedStatus = 0 and RecordStatus = 1 and LastModifiedAt >= @nth
				and LastModifiedAt < @NGAYBDKOAPDUNG_VAT
				and exists (select 1 from @acc where 1=1 and username = td.TK_AdMarket ) 
				union all

				-- lay du lieu sau gio tinh
				select TK_Admarket, DmSanPhamREF, isnull(DmViTriREF,0) DmViTriREF,  SoTienThayDoi AllHopDongTongTCDT
				from ThucChay_PerformanceBase_ThayDoi td
				where DeletedStatus = 0 and RecordStatus = 1 and LastModifiedAt >= @nth
				and LastModifiedAt >= @NGAYBDKOAPDUNG_VAT
				and exists (select 1 from @acc where 1=1 and username = td.TK_AdMarket ) 
	)tc
	group by TK_Admarket, DmSanPhamREF, DmViTriREF

	--select * from @tcdtacc
	-------------3. Lay thuc chay da ghi nhan tcdt cua hopdong

	declare @tcdtacchd table
	(
		SoHopDong nvarchar(50),
		HopDongID int,
		HopDongChiTietREF int,
		username nvarchar(50),
		DmSanPhamREF int,
		TenSanPham nvarchar(500),
		thanhTienPhanBo float,
		DmViTriREF int,
		ThucChayTCDTPhanbo float,
		ThucChayTCDT_KPI FLOAT,
		ThucChay_ThangDuGP FLOAT,
		ThucChayDenNgay datetime
	)
	Insert into @tcdtacchd
	SELECT A.SoHopDong, A.hopDongId, A.phanBoId, A.taiKhoan, A.sanPhamId, A.tenSanPham,A.thanhTienPhanBo,
	isnull(B.DmViTriREF,0) DmViTriREF 
	, ISNULL(B.ThucChay,0) ThucChay
	, ISNULL(B.ThucChay_KPI,0) ThucChay_KPI
	, ISNULL(B.ThucChay_ThangDuGP,0) ThucChay_ThangDuGP
	, B.ThucChayDenNgay
	from (
			SELECT  hd.SoHopDong, hdct.HopDongFK hopDongId,
						hdct.HopDongChiTietID phanBoId,
						hdct.TK_AdMarket taiKhoan,
						hdct.DmSanPhamREF sanPhamId,				   
						hdct.TenSanPham tenSanPham,                
						round(hdct.ThanhTien,0) thanhTienPhanBo 
				FROM dbo.HopDongChiTiet hdct inner join HopDong hd on hdct.HopDongFK = hd.HopDongID
				WHERE 1=1 and hd.HopDongID = @HopDongID
						AND DmSanPhamREF IN ( 144, 585, 628 )
						AND DmLoaiREF <> 42
						AND hdct.deletedstatus = 0 --haidh them vao 20230103 bo phan bo huy
						--AND ChietKhau <> 100
		) A LEFT JOIN 
		( -- du lieu tcdt của pbo
			SELECT tca.HopDongChiTietREF, tca.DmViTriREF
			, SUM(tca.ThucChay) as ThucChay
			, SUM(tca.ThucChay_KPI) as ThucChay_KPI
			, SUM(tca.ThucChay_ThangDuGP) as ThucChay_ThangDuGP
			, MAX(tca.ThucChayDenNgay) ThucChayDenNgay FROM
			(
				  SELECT tcdt.HopDongChiTietREF,
                       tcdt.DmViTriREF,
                       round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) ThucChay,
					   ISNULL(
					   (select round(SUM(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi),0) ThucChay_KPI FROM ThucChayDaTinhAdmarket tc
							WHERE tc.TrangThaiHopDong <> 3
								  AND tc.DmHinhThucQuangCao <> 42
								  and tc.hopdongid = @HopDongID
								  AND tc.DmChienDichREF = 2 --thuc chay tinh cho theo KPI
								  AND tc.HopDongChiTietREF = tcdt.HopDongChiTietREF
								  AND tc.DmViTriREF = tcdt.DmViTriREF
							GROUP BY tc.HopDongChiTietREF,  tc.DmViTriREF
						 ),0) ThucChay_KPI,
						ISNULL(
					   (select round(SUM(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi),0) ThucChay_ThangDuGP FROM ThucChayDaTinhAdmarket tc
							WHERE tc.TrangThaiHopDong <> 3
								  AND tc.DmHinhThucQuangCao <> 42
								  and tc.hopdongid = @HopDongID
								  AND tc.DmChienDichREF = 3 --Thuc chay tinh cho thang du giai phap
								  AND tc.HopDongChiTietREF = tcdt.HopDongChiTietREF
								  AND tc.DmViTriREF = tcdt.DmViTriREF
							GROUP BY tc.HopDongChiTietREF,  tc.DmViTriREF
						 ),0) ThucChay_ThangDuGP,
                       MAX(NgayThucHien) ThucChayDenNgay
                FROM ThucChayDaTinhAdmarket tcdt
                WHERE tcdt.TrangThaiHopDong <> 3
                      AND tcdt.DmHinhThucQuangCao <> 42
					  and tcdt.hopdongid = @HopDongID
                GROUP BY tcdt.HopDongChiTietREF,
                         tcdt.DmViTriREF

			)tca
			GROUP BY tca.HopDongChiTietREF, tca.DmViTriREF
		) B on A.phanBoId = B.HopDongChiTietREF

	--select * from @tcdtacchd

	----------------------------------------------------Bảng tcdt ------------------------------------------------------
	declare @tcdtacchd_all table
	(
	SoHopDong nvarchar(50),
	HopDongID int,
	HopDongChiTietREF int,
		username nvarchar(50),
		DmSanPhamREF int,
		TenSanPham nvarchar(500),
		DmViTriREF_hd int,
		thanhTienPhanBo float,
		ThucChayTCDTPhanbo float,
		ThucChayTCDT_KPI float,
		ThucChay_ThangDuGP  float,
		ThucChayDenNgay DATETIME,
		DmViTriREF int,
		TienChinh_VAT float,
		TienChinh_BF_VAT float,
		AllHopDongTongTCDT float
	)

	insert into @tcdtacchd_all
	select * from
	(
		Select A.* , ISNULL(B.DmViTriREF,0) DmViTriREF, ISNULL(B.TienChinh_VAT,0) TienChinh_VAT, ISNULL(B.TienChinh_BF_VAT,0) TienChinh_BF_VAT, ISNULL(B.AllHopDongTongTCDT,0) AllHopDongTongTCDT from
		(
			select distinct SoHopDong, HopDongID, HopDongChiTietREF, username, DmSanPhamREF, TenSanPham, DmViTriREF as DmViTriREF_hd, thanhTienPhanBo
			, ThucChayTCDTPhanbo, ThucChayTCDT_KPI , ThucChay_ThangDuGP, ThucChayDenNgay
			from @tcdtacchd
		) A
		outer apply
		(
			select a1.DmSanPhamREF, a1.username, a1.DmViTriREF, a1.TienChinh_VAT, a1.TienChinh_BF_VAT, a2.AllHopDongTongTCDT
			from  @tcacc a1 left join @tcdtacc a2 
			on a1.DmViTriREF = a2.DmViTriREF and a1.username = a2.username and a1.DmSanPhamREF = a2.DmSanPhamREF
		)B
		where 1=1 and A.DmSanPhamREF = B.DmSanPhamREF and a.username = B.username
	)a

	--select * from @tcdtacchd_all
	--------------------------bang du lieu
	declare @table1 table
	(  SoHopDong nvarchar(20),
		HopDongID int,
		HopDongChiTietREF int,
		DmSanPhamREF int,
		TenSanPham nvarchar(500),
		TK_Admarket nvarchar(500),
		ThanhTien float,
		DmViTriREF int,
		TenViTri nvarchar(500),
		TienChinh_VAT float, 
		TienChinh_BF_VAT float,
		TienThucChayTong float,
		TienThucChay float,
		TienThucChayKPI FLOAT,
		ThucChay_ThangDuGP FLOAT,
		ThucChayDenNgay datetime,
		[ThucChayConLai] float)

		declare @table2 table
	(  SoHopDong nvarchar(20),
		HopDongID int,
		HopDongChiTietREF int,
		DmSanPhamREF int,
		TenSanPham nvarchar(500),
		TK_Admarket nvarchar(500),
		ThanhTien float,
		DmViTriREF int,
		TenViTri nvarchar(500),
		TienChinh_VAT float, 
		TienChinh_BF_VAT float, 
		TienThucChayTong float,
		TienThucChay float,
		TienThucChayKPI FLOAT,
		ThucChay_ThangDuGP FLOAT,
		ThucChayDenNgay datetime,
		[ThucChayConLai] float)

	insert into @table1

	SELECT T1.SoHopDong, T1.HopDongID, T1.HopDongChiTietREF
	, T1.DmSanPhamREF, T1.TenSanPham, T1.username
	, T1.thanhTienPhanBo
	, T1.DmViTriREF
	, 			(CASE
								WHEN  t1.DmViTriREF = 1 THEN
									'AdX'
								WHEN  t1.DmViTriREF = 2 THEN
									'AdX Mobile'
								WHEN  t1.DmViTriREF = 3 THEN
									'AdX Ecommerce'
								WHEN  t1.DmViTriREF = 4 THEN
									'AdX LeadForm'
								WHEN  t1.DmViTriREF = 0 THEN
									''
								ELSE
									''
							END
							)  TenViTri 
	, T1.TienChinh_VAT
	, T1.TienChinh_BF_VAT
	, T1.AllHopDongTongTCDT
	, T1.ThucChayTCDTPhanbo
	, T1.ThucChayTCDT_KPI
	, T1.ThucChay_ThangDuGP
	, T1.ThucChayDenNgay
	, (t1.TienChinh_BF_VAT-(isnull(t1.AllHopDongTongTCDT,0)- isnull(T1.ThucChayTCDT_KPI,0) - isnull(T1.ThucChay_ThangDuGP,0)) ) AS [ThucChayConLai]
	FROM @tcdtacchd_all T1
	WHERE T1.DmViTriREF = T1.DmViTriREF_hd

	INSERT INTO @table2
	        ( SoHopDong ,
	          HopDongID ,
	          HopDongChiTietREF ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          TK_Admarket ,
	          ThanhTien ,
	          DmViTriREF ,
	          TenViTri ,
	          TienChinh_VAT ,
			  TienChinh_BF_VAT ,
	          TienThucChayTong ,
	          TienThucChay ,
	          TienThucChayKPI ,
			  ThucChay_ThangDuGP ,
	          ThucChayDenNgay ,
	          ThucChayConLai
	        )
	SELECT SoHopDong ,
           HopDongID ,
           HopDongChiTietREF ,
           DmSanPhamREF ,
           TenSanPham ,
           TK_Admarket ,
           ThanhTien ,
           DmViTriREF ,
           TenViTri ,
           TienChinh_VAT ,
		   TienChinh_BF_VAT ,
           TienThucChayTong ,
           TienThucChay ,
           TienThucChayKPI ,
		   ThucChay_ThangDuGP ,
           ThucChayDenNgay ,
           ThucChayConLai FROM @table1
	UNION ALL
	SELECT DISTINCT T1.SoHopDong, T1.HopDongID, T1.HopDongChiTietREF
	, T1.DmSanPhamREF, T1.TenSanPham, T1.username
	, T1.thanhTienPhanBo
	, T1.DmViTriREF
	, 			(CASE
								WHEN  t1.DmViTriREF = 1 THEN
									'AdX'
								WHEN  t1.DmViTriREF = 2 THEN
									'AdX Mobile'
								WHEN  t1.DmViTriREF = 3 THEN
									'AdX Ecommerce'
								WHEN  t1.DmViTriREF = 4 THEN
									'AdX LeadForm'
								WHEN  t1.DmViTriREF = 0 THEN
									''
								ELSE
									''
							END
							)  TenViTri 
	, T1.TienChinh_VAT
	, T1.TienChinh_BF_VAT
	, ISNULL(T1.AllHopDongTongTCDT,0) AllHopDongTongTCDT
	, 0 as ThucChayTCDTPhanbo
	, ISNULL(T1.ThucChayTCDT_KPI,0) ThucChayTCDT_KPI
	, ISNULL(T1.ThucChay_ThangDuGP,0) ThucChay_ThangDuGP
	, ISNULL(T1.ThucChayDenNgay,'1900-01-01')
	,  (t1.TienChinh_BF_VAT-(isnull(t1.AllHopDongTongTCDT,0)- isnull(T1.ThucChayTCDT_KPI,0) - isnull(T1.ThucChay_ThangDuGP,0)) ) AS [ThucChayConLai]
	--(t1.TienChinh_BF_VAT-isnull(t1.AllHopDongTongTCDT,0)) AS [ThucChayConLai]
	FROM @tcdtacchd_all T1
	WHERE 1=1
	AND ISNULL(T1.DmViTriREF,0) <> ISNULL(T1.DmViTriREF_hd,0)
	AND NOT EXISTS(SELECT TOP (1) t.DmSanPhamREF FROM @table1 t
	WHERE t.HopDongChiTietREF = t1.HopDongChiTietREF
	AND t.DmSanPhamREF = t1.DmSanPhamREF
	AND t.TK_Admarket = t1.UserName
	AND t.DmViTriREF = t1.DmViTriREF ORDER BY t.HopDongChiTietREF)

	UNION ALL
	--2. LAY DU LIEU CUA CAC SAN PHAM KO PHAI CUA ADMARKET
	---Xac dinh thong tin hop hop dong
	SELECT hdct.SoHopDong, hdct.HopDongID, hdct.HopDongChiTietREF
		, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.TK_Admarket, hdct.ThanhTien 
		, 0 DmViTriREF, '' TenViTri, 0 TienChinh_AF_VAT, 0 TienChinh_VAT
		, 0 TienThucChayTong, ISNULL(tc.TienThucChay,0) TienThucChay, ISNULL(tc.TienThucChay_KPI,0) TienThucChay_KPI
		, ISNULL(tc.ThucChay_ThangDuGP,0) ThucChay_ThangDuGP, ISNULL(tc.ThucChayDenNgay,'1900-01-01') ThucChayDenNgay
		, 0 ThucChayConLai
	FROM
	(
		SELECT hd.SoHopDong AS SoHopDong, hdct.HopDongFK AS HopDongID, hdct.HopDongChiTietID as HopDongChiTietREF
		, hdct.DmSanPhamREF, hdct.TenSanPham, '' TK_Admarket, hdct.ThanhTien
		FROM dbo.HopDongChiTiet hdct
		INNER JOIN dbo.Hopdong hd on hdct.HopDongFK = hd.HopDongID
		WHERE hdct.HopDongFK = @HopDongID
		AND (hdct.DmLoaiREF in (26,5010,5000,5038) --Self-serving,Performance Service,Performance Package
		OR (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_MKT_FEE))
		AND hdct.DmSanPhamREF NOT IN (144,585,628,306,423,5188)--HAIDH Update 04/03/2023 them các san pham facebooking, tiktok
		AND hdct.deletedstatus = 0 --haidh them vao loai phan bo bị huy
		
	)hdct
	LEFT JOIN 
	(
		SELECT tca.HopDongChiTietREF
			, SUM(tca.ThucChay) as TienThucChay
			, SUM(tca.ThucChay_KPI) as TienThucChay_KPI
			, SUM(tca.ThucChay_ThangDuGP) as ThucChay_ThangDuGP
			, MAX(tca.ThucChayDenNgay) ThucChayDenNgay FROM
			(
				  SELECT tcdt.HopDongChiTietREF,
				  (CASE WHEN tcdt.DmChienDichREF = 3 THEN round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0)
					ELSE 0
				  END) ThucChay_ThangDuGP
				  , round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) ThucChay
				  , 0 ThucChay_KPI
				  ,	MAX(NgayThucHien) ThucChayDenNgay
                FROM ThucChayDaTinh tcdt
                WHERE tcdt.TrangThaiHopDong <> 3
                      AND tcdt.DmHinhThucQuangCao IN (26,5010,5000,5038)
					  AND tcdt.DmSanPhamREF NOT IN (144,585,628,306,423,5188) --HAIDH Update 04/03/2023 them các san pham facebooking, tiktok
					  and tcdt.hopdongid = @HopDongID
                GROUP BY tcdt.HopDongChiTietREF, tcdt.DmChienDichREF
			)tca
			GROUP BY tca.HopDongChiTietREF
	)tc on tc.HopDongChiTietREF = hdct.HopDongChiTietREF

	SELECT SoHopDong ,
           HopDongID ,
           HopDongChiTietREF ,
           DmSanPhamREF ,
           TenSanPham ,
           TK_Admarket ,
           ThanhTien ,
           DmViTriREF ,
           TenViTri ,
           TienChinh_VAT AS TienChinh_AF_VAT,
		   TienChinh_BF_VAT AS TienChinh_VAT,
           TienThucChayTong ,
           TienThucChay ,
           TienThucChayKPI ,
		   ThucChay_ThangDuGP ,
           ThucChayDenNgay ,
           ThucChayConLai FROM @table2
	ORDER BY HopDongChiTietREF, DmViTriREF
	
END

```
