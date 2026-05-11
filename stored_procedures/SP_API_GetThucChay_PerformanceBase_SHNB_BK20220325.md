# Stored Procedure: `API_GetThucChay_PerformanceBase_SHNB_BK20220325`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-03-25 16:15:20.713000
- **Ngày sửa cuối**: 2022-03-25 16:15:20.713000

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
--[dbo].[API_GetThucChay_PerformanceBase_SHNB] N'SH0050821'
-- =============================================
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_SHNB_BK20220325] 
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	 DECLARE @HopDongID INT;
	DECLARE @nth2 datetime;

    SELECT @HopDongID = HopDongID FROM HopDong WHERE SoHopDong = @SoHopDong
	SELECT @nth2 = convert(Date,dateadd(day,-1,getdate()))
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
	--select @nth2
--------------------------------------------------1. Lay thuc chay do team san pham tra ve cua acc------------------------------------------
	Declare @tcacc  table
	(
	username nvarchar(50),
	DmSanPhamREF int,
	DmViTriREF int,
	TienChinh_VAT float
	)
	Insert into @tcacc
	--adx	
	select tcdta1.username,  tcdta1.DmSanPhamREF,  tcdta1.DmViTriREF
	, 0 TienChinh_VAT
	--, tcdta1.TienChinh_VAT
	FROM dbo.[ThucChay_CPCAdmarket_ViewAll] tcdta1 
	WHERE 1=1 AND  exists (select 1 from @acc where 1=1
					--and DmSanPhamREF = tcdta1.DmSanPhamREF
					and username = tcdta1.username
					) 

	--select * from @tcacc
		-- Insert statements for procedure here
	-------------2. Lay thuc chay da ghi nhan tcdt cua acc
	declare @tcdtacc table
	(
		username nvarchar(50),
		DmSanPhamREF int,
		DmViTriREF int,
		TongTCDT_VAT float
	)
	Insert into @tcdtacc
	select tc.TK_AdMarket,tc.DmSanPhamREF,tc.DmViTriREF,  0 AS TongTCDT_VAT  from (
	SELECT tcdt.TK_AdMarket,
					   tcdt.DmSanPhamREF,
					   tcdt.DmViTriREF,
					   tcdt.TongTCDT_VAT
				FROM [dbo].[ThucChayDaTinh_CPCMAdmarket_NBSH_Viewll] tcdt
				where exists (select 1 from @acc where 1=1
						--and DmSanPhamREF = tcdta1.DmSanPhamREF
						and username = tcdt.TK_AdMarket
						) 

	union all

	select TK_Admarket, DmSanPhamREF, DmViTriREF,  SoTienThayDoi TongTCDT_VAT 
	from ThucChay_PerformanceBase_ThayDoi td
	where DeletedStatus = 0 --and RecordStatus = 0
	and exists (select 1 from @acc where 1=1
						and username = td.TK_AdMarket
						) 
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
		TenSanPham nvarchar(50),
		thanhTienPhanBoVAT float,
		DmViTriREF int,
		ThucChayTCDTPhanbo_VAT float,
		ThucChayTCDT_KPI_VAT float,
		ThucChayDenNgay datetime
	)
	Insert into @tcdtacchd
	SELECT A.SoHopDong, A.hopDongId, A.phanBoId, A.taiKhoan, A.sanPhamId, A.tenSanPham,A.thanhTienPhanBoVAT,
	B.DmViTriREF,B.ThucChayVAT, B.ThucChay_KPI_VAT,B.ThucChayDenNgay
	from (
	  SELECT  hd.SoHopDong,
	  hdct.HopDongFK hopDongId,
					   hdct.HopDongChiTietID phanBoId,
					   hdct.DeletedStatus,
					   hdct.TK_AdMarket taiKhoan,
					   hdct.DmSanPhamREF sanPhamId,				   
					   hdct.TenSanPham tenSanPham,                
					   round(hdct.ThanhTien*1.1,0) thanhTienPhanBoVAT 
				FROM dbo.HopDongChiTiet hdct inner join HopDong hd on hdct.HopDongFK = hd.HopDongID
				WHERE 1=1 and hd.HopDongID = @HopDongID
					  --exists (select 1 from @dshd where 1=1 and HopDongChiTietID = hdct.HopDongChiTietID)
					  AND DmSanPhamREF IN ( 144, 585, 628 )
					  AND DmLoaiREF <> 42
					  AND ChietKhau <> 100
			) A LEFT JOIN 
			( -- du lieu tcdt của pbo
				SELECT tca.HopDongChiTietREF, tca.DmViTriREF
				, SUM(tca.ThucChayVAT) as ThucChayVAT
				, SUM(tca.ThucChay_KPI_VAT) as ThucChay_KPI_VAT
				, MAX(tca.ThucChayDenNgay) ThucChayDenNgay FROM
				(
					  SELECT tcdt.HopDongChiTietREF,
						   tcdt.DmViTriREF,
						   round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)*1.1,0) ThucChayVAT,
						   ISNULL((select round(SUM(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi)*1.1,0) ThucChay_KPI_VAT FROM ThucChayDaTinhAdmarket tc
								WHERE tc.TrangThaiHopDong <> 3
									  AND tc.DmHinhThucQuangCao <> 42
									  and tc.hopdongid = @HopDongID
									  AND tc.DmChienDichREF = 2
									  AND tc.HopDongChiTietREF = tcdt.HopDongChiTietREF
								GROUP BY tc.HopDongChiTietREF,  tc.DmViTriREF
							 ),0) ThucChay_KPI_VAT,
						   MAX(NgayThucHien) ThucChayDenNgay
					FROM ThucChayDaTinhAdmarket tcdt
					WHERE tcdt.TrangThaiHopDong <> 3
						  AND tcdt.DmHinhThucQuangCao <> 42
						  and tcdt.hopdongid = @HopDongID
					GROUP BY tcdt.HopDongChiTietREF,
							 tcdt.DmViTriREF

				)tca
				GROUP BY tca.HopDongChiTietREF, tca.DmViTriREF
			) B
			on A.phanBoId = B.HopDongChiTietREF
			WHERE NOT (A.DeletedStatus = 1 AND B.ThucChay_KPI_VAT <> 0)
		--select * from @tcdtacchd
	----------------------------------------------------Bảng tcdt ------------------------------------------------------
	declare @tcdtacchd_all table
	(
	SoHopDong nvarchar(50),
	HopDongID int,
	HopDongChiTietREF int,
		username nvarchar(50),
		DmSanPhamREF int,
		TenSanPham nvarchar(50),
		DmViTriREF_hd int,
		thanhTienPhanBoVAT float,
		ThucChayTCDTPhanbo_VAT float,
		ThucChayTCDT_KPI_VAT float,
		ThucChayDenNgay datetime,
		DmViTriREF int,
		TienChinh_VAT float,
		ThucChayTCDT_VAT float
	)

	insert into @tcdtacchd_all
	select * from
	(
		Select A.* , B.DmViTriREF, B.TienChinh_VAT, B.TongTCDT_VAT from
		(
			select distinct SoHopDong, HopDongID, HopDongChiTietREF, username, DmSanPhamREF, TenSanPham, DmViTriREF as DmViTriREF_hd, thanhTienPhanBoVAT, ThucChayTCDTPhanbo_VAT, ThucChayTCDT_KPI_VAT , ThucChayDenNgay
			from @tcdtacchd
		) A
		outer apply
		(
			select a1.DmSanPhamREF, a1.username, a1.DmViTriREF, a1.TienChinh_VAT, a2.TongTCDT_VAT
			from  @tcacc a1 left join @tcdtacc a2 
			on a1.DmViTriREF = a2.DmViTriREF and a1.username = a2.username and a1.DmSanPhamREF = a2.DmSanPhamREF
		)B
		where 1=1 and A.DmSanPhamREF = B.DmSanPhamREF and a.username = B.username
	)a

	--select * from @tcdtacchd_all
	------------------------bang du lieu
	declare @table1 table
	(  SoHopDong nvarchar(20),
	   HopDongID int,
	   HopDongChiTietREF int,
	   DmSanPhamREF int,
	   TenSanPham nvarchar(20),
	   TK_Admarket nvarchar(50),
	   ThanhTien float,
	   DmViTriREF int,
	   TenViTri nvarchar(20),
	   TienChinh_VAT float, 
	   TienThucChayTong float,
	   TienThucChay float,
	   TienThucChay_KPI float,
	   ThucChayDenNgay datetime,
	   [ThucChayConLai] float)

	   declare @table2 table
	(  SoHopDong nvarchar(20),
	   HopDongID int,
	   HopDongChiTietREF int,
	   DmSanPhamREF int,
	   TenSanPham nvarchar(20),
	   TK_Admarket nvarchar(50),
	   ThanhTien float,
	   DmViTriREF int,
	   TenViTri nvarchar(20),
	   TienChinh_VAT float, 
	   TienThucChayTong float,
	   TienThucChay float,
	   TienThucChay_KPI float,
	   ThucChayDenNgay datetime,
	   [ThucChayConLai] float)

	insert into @table1
	SELECT T1.SoHopDong, T1.HopDongID, T1.HopDongChiTietREF
	, T1.DmSanPhamREF, T1.TenSanPham, T1.username
	, T1.thanhTienPhanBoVAT
	, T1.DmViTriREF
	, 			(CASE
								WHEN  t1.DmViTriREF = 1 THEN
									'AdX'
								WHEN  t1.DmViTriREF = 2 THEN
									'AdX Mobile'
								WHEN  t1.DmViTriREF = 3 THEN
									'AdX Ecommerce'
								WHEN  t1.DmViTriREF = 0 THEN
									''
								ELSE
									''
							END
							)  TenViTri 
	, T1.TienChinh_VAT
	, isnull(T1.ThucChayTCDT_VAT,0) ThucChayTCDT_VAT
	, isnull(T1.ThucChayTCDTPhanbo_VAT,0) ThucChayTCDTPhanbo_VAT
	, isnull(T1.ThucChayTCDT_KPI_VAT,0) ThucChayTCDT_KPI_VAT
	, T1.ThucChayDenNgay
	, (t1.TienChinh_VAT-isnull(t1.ThucChayTCDT_VAT,0)) AS [ThucChayConLai]
	FROM @tcdtacchd_all T1
	WHERE isnull(T1.DmViTriREF,0) = isnull(T1.DmViTriREF_hd,0)

	
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
	          TienThucChayTong ,
	          TienThucChay ,
	          TienThucChay_KPI ,
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
           TienThucChayTong ,
           TienThucChay ,
           TienThucChay_KPI ,
           ThucChayDenNgay ,
           ThucChayConLai FROM @table1
	UNION ALL
	SELECT DISTINCT T1.SoHopDong, T1.HopDongID, T1.HopDongChiTietREF
	, T1.DmSanPhamREF, T1.TenSanPham, T1.username
	, T1.thanhTienPhanBoVAT
	, T1.DmViTriREF
	, 			(CASE
								WHEN  t1.DmViTriREF = 1 THEN
									'AdX'
								WHEN  t1.DmViTriREF = 2 THEN
									'AdX Mobile'
								WHEN  t1.DmViTriREF = 3 THEN
									'AdX Ecommerce'
								WHEN  t1.DmViTriREF = 0 THEN
									''
								ELSE
									''
							END
							)  TenViTri 
	, T1.TienChinh_VAT
	, isnull(T1.ThucChayTCDT_VAT,0) ThucChayTCDT_VAT
	, 0 as ThucChayTCDTPhanbo_VAT
	, T1.ThucChayTCDT_KPI_VAT
	, T1.ThucChayDenNgay
	, (t1.TienChinh_VAT-isnull(t1.ThucChayTCDT_VAT,0)) AS [ThucChayConLai]
	FROM @tcdtacchd_all T1
	WHERE 1=1
	AND ISNULL(T1.DmViTriREF,0) <> ISNULL(T1.DmViTriREF_hd,0)
	AND NOT EXISTS(SELECT TOP (1) t.DmSanPhamREF FROM @table1 t
	WHERE t.HopDongChiTietREF = t1.HopDongChiTietREF
	AND t.DmSanPhamREF = t1.DmSanPhamREF
	AND t.TK_Admarket = t1.UserName
	AND t.DmViTriREF = t1.DmViTriREF ORDER BY t.HopDongChiTietREF)

	-- select du lieu
	select SoHopDong ,
           HopDongID ,
           HopDongChiTietREF ,
           DmSanPhamREF ,
           TenSanPham ,
           TK_Admarket ,
           ThanhTien ,
           DmViTriREF ,
           TenViTri ,
           TienChinh_VAT ,
           TienThucChayTong ,
           TienThucChay ,
           TienThucChay_KPI ,
           ThucChayDenNgay ,
           ThucChayConLai from @table2	
	order by HopDongChiTietREF, DmViTriREF
END

```
