# Stored Procedure: `API_GetThucChay_PerformanceBase_Test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-12 10:02:13.240000
- **Ngày sửa cuối**: 2021-05-17 15:25:10.647000

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
--[API_GetThucChay_PerformanceBase_Test] N'qc5870320'
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_Test]
    -- Add the parameters for the stored procedure here
    @SoHopDong NVARCHAR(50)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
	
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
select tcdta1.username,  tcdta1.DmSanPhamREF,  tcdta1.DmViTriREF, tcdta1.TienChinh_VAT
FROM dbo.[ThucChay_CPCAdmarket_ViewAll] tcdta1 
WHERE 1=1 AND  exists (select 1 from @acc where 1=1
					--and DmSanPhamREF = tcdta1.DmSanPhamREF
					and username = tcdta1.username
					) 

--select * from @tcacc
    -- Insert statements for procedure here
-------------2. Lay thuc chay da ghi nhan tcdt cua acc

declare @ngaythuchien nvarchar(50), @nth datetime
select @ngaythuchien = CONVERT(VARCHAR(10),convert(date,getdate(),103),111) + ' 12:01:00'
set @nth =  (select convert(datetime, @ngaythuchien))



declare @tcdtacc table
(
	username nvarchar(50),
	DmSanPhamREF int,
	DmViTriREF int,
	TongTCDT_VAT float
)
Insert into @tcdtacc
select tc.TK_AdMarket,tc.DmSanPhamREF,tc.DmViTriREF, sum(TongTCDT_VAT)TongTCDT_VAT  from (
SELECT tcdt.TK_AdMarket,
                   tcdt.DmSanPhamREF,
                   tcdt.DmViTriREF,
                   tcdt.TongTCDT_VAT
            FROM [ThucChayDaTinh_CPCAdmarket_ViewAll] tcdt
			where exists (select 1 from @acc where 1=1
					--and DmSanPhamREF = tcdta1.DmSanPhamREF
					and username = tcdt.TK_AdMarket
					) 

union all

select TK_Admarket, DmSanPhamREF, DmViTriREF,  SoTienThayDoi TongTCDT_VAT 
from ThucChay_PerformanceBase_ThayDoi td
where DeletedStatus = 0 and RecordStatus = 1 and LastModifiedAt < @nth
and exists (select 1 from @acc where 1=1
					and username = td.TK_AdMarket
					) 

union all

select TK_Admarket, DmSanPhamREF, DmViTriREF,  SoTienThayDoi TongTCDT_VAT 
from ThucChay_PerformanceBase_ThayDoi td
where DeletedStatus = 0 and RecordStatus = 0 and LastModifiedAt >= @nth
and exists (select 1 from @acc where 1=1
					and username = td.TK_AdMarket
					) 

)tc
group by TK_Admarket, DmSanPhamREF, DmViTriREF

--select * from @tcdtacc
-------------3. Lay thuc chay da ghi nhan tcdt cua hopdong
declare @dshd table
(HopDongChiTietID int
)
insert into @dshd
select HopDongChiTietID from HopDongChiTiet hdct inner join HopDong hd
on hdct.HopDongFK = HopDongID
where 1=1 and exists (select 1 from @acc where 1=1 and hdct.TK_AdMarket = username )
and DmSanPhamREF in (144,585,628) and hdct.DeletedStatus = 0 and DmLoaiREF not in ( 42,13)
and TrangThaiHopDong <> 3
--loai hd NB,SH
and DmMaHopDongREF not in (310,533)
and HopDongID = @HopDongID

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
	ThucChayTCDT_VAT float,
	ThucChayDenNgay datetime
)
Insert into @tcdtacchd
SELECT A.SoHopDong, A.hopDongId, A.phanBoId, A.taiKhoan, A.sanPhamId, A.tenSanPham,A.thanhTienPhanBoVAT,
B.DmViTriREF,B.ThucChayVAT,B.ThucChayDenNgay
from (
  SELECT  hd.SoHopDong,
  hdct.HopDongFK hopDongId,
                   hdct.HopDongChiTietID phanBoId,
				   hdct.TK_AdMarket taiKhoan,
                   hdct.DmSanPhamREF sanPhamId,				   
                   hdct.TenSanPham tenSanPham,                
                   round(hdct.ThanhTien*1.1,0) thanhTienPhanBoVAT 
            FROM dbo.HopDongChiTiet hdct inner join HopDong hd on hdct.HopDongFK = hd.HopDongID
            WHERE 1=1 and hd.HopDongID = @HopDongID
			      --exists (select 1 from @dshd where 1=1 and HopDongChiTietID = hdct.HopDongChiTietID)
                  AND DmSanPhamREF IN ( 144, 585, 628 )
                  AND DmLoaiREF <> 42
        ) A LEFT JOIN ( -- du lieu tcdt của pbo
                SELECT HopDongChiTietREF,
                       DmViTriREF,
                       round(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)*1.1,0) ThucChayVAT,
                       MAX(NgayThucHien) ThucChayDenNgay
                FROM ThucChayDaTinhAdmarket
                WHERE TrangThaiHopDong <> 3
                      AND DmHinhThucQuangCao <> 42
					  and hopdongid = @HopDongID
                GROUP BY HopDongChiTietREF,
                         DmViTriREF
                        -- ,TenViTri, TenDangNhap,TenNhanVien
						 ) B
						 on A.phanBoId = B.HopDongChiTietREF
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
	thanhTienPhanBoVAT float,
	DmViTriREF int,
	ThucChayTCDT_VAT float,
	ThucChayDenNgay datetime
)
/*
insert into @tcdtacchd_all
select * from @tcdtacchd where DmViTriREF is not null 
insert into @tcdtacchd_all
select A.* from (
select SoHopDong, HopDongID, HopDongChiTietREF, username, DmSanPhamREF, TenSanPham, thanhTienPhanBoVAT,t.DmViTriREF,t.ThucChayTCDT_VAT,t.ThucChayDenNgay
from @tcdtacchd t1
outer apply
(select distinct DmViTriREF,0 ThucChayTCDT_VAT,null ThucChayDenNgay  from @tcacc t2 where t1.DmSanPhamREF = t2.DmSanPhamREF) t
where t1.DmViTriREF is null
)A
*/

insert into @tcdtacchd_all
Select A.*, B.DmViTriREF , B.ThucChayTCDT_VAT,B.ThucChayDenNgay from
(
select distinct SoHopDong, HopDongID, HopDongChiTietREF, username, DmSanPhamREF, TenSanPham, thanhTienPhanBoVAT from 
@tcdtacchd
) A
left join
(
--select * from @tcacc
select a1.DmViTriREF , a2.ThucChayTCDT_VAT,a2.ThucChayDenNgay,a1.DmSanPhamREF
from  @tcacc a1 left join @tcdtacchd a2 on a1.DmViTriREF = a2.DmViTriREF
)B
on 1=1 and A.DmSanPhamREF = B.DmSanPhamREF


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
   ThucChayDenNgay datetime,
   [ThucChayConLai] float)

insert into @table1

select --t1.username, t1.DmSanPhamREF, t1.DmViTriREF, t1.TienChinh_VAT, t2.TongTCDT_VAT, t3.ThucChayTCDT_VAT, (t1.TienChinh_VAT-t2.TongTCDT_VAT)[ThucChayConLai]
  t3.SoHopDong,
           t3.HopDongID,
           t3.HopDongChiTietREF,
           t3.DmSanPhamREF,
           t3.TenSanPham,
           t1.username TK_Admarket,
           round(thanhTienPhanBoVAT,0) ThanhTien,
           t1.DmViTriREF,
           (CASE
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
                       )  TenViTri ,
		   t1.TienChinh_VAT, 
           t2.TongTCDT_VAT TienThucChayTong,
           t3.ThucChayTCDT_VAT TienThucChay,
           t3.ThucChayDenNgay,
		   (t1.TienChinh_VAT-isnull(t2.TongTCDT_VAT,0))[ThucChayConLai]
from @tcacc t1 full outer join @tcdtacc t2
on t1.username = t2.username 
and t1.DmSanPhamREF = t2.DmSanPhamREF
and t1.DmViTriREF = t2.DmViTriREF
full outer join @tcdtacchd_all t3
--@tcdtacchd t3
on t1.username = t3.username
and (t1.DmSanPhamREF = t3.DmSanPhamREF or t3.DmSanPhamREF is null)
and t1.DmViTriREF = t3.DmViTriREF
where 1=1 and SoHopDong = @SoHopDong


/*
--table2 de tinh tong theo hdct
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
   ThucChayDenNgay datetime,
   [ThucChayConLai] float)
   insert into @table2
select SoHopDong ,
   HopDongID ,
   HopDongChiTietREF ,
   DmSanPhamREF ,
   TenSanPham ,
   TK_Admarket ,
   ThanhTien , 
   0,'',0,0,
   sum(TienThucChay) TienThucChay
   ,max(ThucChayDenNgay),0
   from @table1
   group by SoHopDong ,
   HopDongID ,
   HopDongChiTietREF ,
   DmSanPhamREF ,
   TenSanPham ,
   TK_Admarket,
   ThanhTien


-- select du lieu
select * from @table1	
union all
select * from @table2
*/
-- select du lieu
select * from @table1	
order by DmSanPhamREF, HopDongID, HopDongChiTietREF
	
END;





```
