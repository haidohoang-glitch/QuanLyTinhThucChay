# Stored Procedure: `API_GetThucChay_PerformanceBase_SHNB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-17 14:20:11.100000
- **Ngày sửa cuối**: 2022-04-01 11:10:51.500000

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
--[dbo].[API_GetThucChay_PerformanceBase_SHNB] N'S-NB0010122'
-- =============================================
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_SHNB] 
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
	DECLARE @NGAYBDKOAPDUNG_VAT DATETIME = '2022-03-29' --ngay ap dung vat

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
	--select * from @acc
--------------------------------------------------1. Lay thuc chay do team san pham tra ve cua acc------------------------------------------
	Declare @tcacc  table
	(
	username nvarchar(50),
	DmSanPhamREF int,
	DmViTriREF int,
	TienChinh_VAT float,
	TienChinh_BF_VAT float
	)
	Insert into @tcacc
	--adx	
	select tcdta1.username,  tcdta1.DmSanPhamREF,  tcdta1.DmViTriREF
	, 0 TienChinh_VAT
	, 0 TienChinh_bf_vat
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
		TongTCDT float
	)
	Insert into @tcdtacc
	select tc.TK_AdMarket,tc.DmSanPhamREF,tc.DmViTriREF,  0 AS TongTCDT  from (
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
		thanhTienPhanBo float,
		DmViTriREF int,
		ThucChayTCDTPhanbo float,
		ThucChayTCDT_KPI float,
		ThucChayDenNgay datetime
	)
	Insert into @tcdtacchd
	SELECT A.SoHopDong, A.hopDongId, A.phanBoId, A.taiKhoan, A.sanPhamId, A.tenSanPham,A.thanhTienPhanBo,
	B.DmViTriREF,B.ThucChay, B.ThucChay_KPI,B.ThucChayDenNgay
	from (
	  SELECT  hd.SoHopDong,
	  hdct.HopDongFK hopDongId,
					   hdct.HopDongChiTietID phanBoId,
					   hdct.DeletedStatus,
					   hdct.TK_AdMarket taiKhoan,
					   hdct.DmSanPhamREF sanPhamId,				   
					   hdct.TenSanPham tenSanPham,                
					   round(hdct.ThanhTien,0) thanhTienPhanBo
				FROM dbo.HopDongChiTiet hdct inner join HopDong hd on hdct.HopDongFK = hd.HopDongID
				WHERE 1=1 and hd.HopDongID = @HopDongID
					  --exists (select 1 from @dshd where 1=1 and HopDongChiTietID = hdct.HopDongChiTietID)
					  AND DmSanPhamREF IN ( 144, 585, 628 )
					  AND DmLoaiREF <> 42
					  AND ChietKhau <> 100
			) A LEFT JOIN 
			( -- du lieu tcdt của pbo
				SELECT tca.HopDongChiTietREF, tca.DmViTriREF
				, SUM(tca.ThucChay) as ThucChay
				, SUM(tca.ThucChay_KPI) as ThucChay_KPI
				, MAX(tca.ThucChayDenNgay) ThucChayDenNgay FROM
				(
					  SELECT tcdt.HopDongChiTietREF,
						   tcdt.DmViTriREF,
						   round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) ThucChay,
						   ISNULL((select round(SUM(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi),0) ThucChay_KPI FROM ThucChayDaTinhAdmarket tc
								WHERE tc.TrangThaiHopDong <> 3
									  AND tc.DmHinhThucQuangCao <> 42
									  and tc.hopdongid = @HopDongID
									  AND tc.DmChienDichREF = 2
									  AND tc.HopDongChiTietREF = tcdt.HopDongChiTietREF
								GROUP BY tc.HopDongChiTietREF,  tc.DmViTriREF
							 ),0) ThucChay_KPI,
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
			WHERE NOT (A.DeletedStatus = 1 AND B.ThucChay_KPI <> 0)
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
		thanhTienPhanBo float,
		ThucChayTCDTPhanbo float,
		ThucChayTCDT_KPI float,
		ThucChayDenNgay datetime,
		DmViTriREF int,
		TienChinh_VAT float,
		TienChinh_bf_VAT float,
		ThucChayTCDT float
	)

	insert into @tcdtacchd_all
	select * from
	(
		Select A.* , B.DmViTriREF, B.TienChinh_VAT, b.TienChinh_bf_VAT, B.TongTCDT from
		(
			select distinct SoHopDong, HopDongID, HopDongChiTietREF, username, DmSanPhamREF, TenSanPham, DmViTriREF as DmViTriREF_hd, thanhTienPhanBo, ThucChayTCDTPhanbo, ThucChayTCDT_KPI , ThucChayDenNgay
			from @tcdtacchd
		) A
		outer apply
		(
			select a1.DmSanPhamREF, a1.username, a1.DmViTriREF, a1.TienChinh_VAT, a1.TienChinh_bf_VAT, a2.TongTCDT
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
	   TienChinh_bf_VAT float, 
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
	   TienChinh_bf_VAT float, 
	   TienThucChayTong float,
	   TienThucChay float,
	   TienThucChay_KPI float,
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
								WHEN  t1.DmViTriREF = 0 THEN
									''
								ELSE
									''
							END
							)  TenViTri 
	, T1.TienChinh_VAT
	, T1.TienChinh_bf_VAT
	, isnull(T1.ThucChayTCDT,0) ThucChayTCDT
	, isnull(T1.ThucChayTCDTPhanbo,0) ThucChayTCDTPhanbo
	, isnull(T1.ThucChayTCDT_KPI,0) ThucChayTCDT_KPI
	, T1.ThucChayDenNgay
	, (t1.TienChinh_bf_VAT-isnull(t1.ThucChayTCDT,0)) AS [ThucChayConLai]
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
			  TienChinh_bf_VAT ,
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
		   TienChinh_BF_VAT ,
           TienThucChayTong ,
           TienThucChay ,
           TienThucChay_KPI ,
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
								WHEN  t1.DmViTriREF = 0 THEN
									''
								ELSE
									''
							END
							)  TenViTri 
	, T1.TienChinh_VAT
	, T1.TienChinh_BF_VAT
	, isnull(T1.ThucChayTCDT,0) ThucChayTCDT
	, 0 as ThucChayTCDTPhanbo
	, T1.ThucChayTCDT_KPI
	, T1.ThucChayDenNgay
	, (t1.TienChinh_BF_VAT-isnull(t1.ThucChayTCDT,0)) AS [ThucChayConLai]
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
           TienChinh_VAT AS TienChinh_AF_VAT,
		   TienChinh_BF_VAT AS TienChinh_VAT,
           TienThucChayTong ,
           TienThucChay ,
           TienThucChay_KPI ,
           ThucChayDenNgay ,
           ThucChayConLai from @table2	
	order by HopDongChiTietREF, DmViTriREF
END

```
