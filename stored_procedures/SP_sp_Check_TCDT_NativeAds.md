# Stored Procedure: `sp_Check_TCDT_NativeAds`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-20 10:55:27.270000
- **Ngày sửa cuối**: 2021-06-11 16:37:04.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_Check_TCDT_NativeAds 5133,'2021-05-18'
CREATE proc [dbo].[sp_Check_TCDT_NativeAds]
 @DmSanPhamREF int,
 @NgayThucHien datetime
as
Begin
Declare @TypeProduct int
IF @DmSanPhamREF = 821 
	set @TypeProduct = 19
else if @DmSanPhamREF = 5133 
	set @TypeProduct = 5133
else set @TypeProduct = 0

select A1.* from(
select B.HopDongID, A.Sohopdong,A.ThoiGianSuaHopDong,A.ThanhTien,A.TienKM,A.tthd,A.tthdkm,B.SoHopDong shd, B.tc, B.km,
(case when A.ThanhTien >=A.tthd then A.tthd - B.tc else A.ThanhTien - B.tc end)lechtc, 
(case when A.TienKM >=A.tthdkm then A.tthdkm - B.km else A.TienKM - B.km end)lechkm
from (
		select TC.*, HD.ThoiGianSuaHopDong,HD.tthd,HD.tthdkm  from (
		SELECT Sohopdong, 
		SUM(tc.SoLuongThucchay) SoLuongThucchay, SUM(tc.SoLuongThucchayKM) SoLuongKM,sum(ThanhTienThucchaySauCK) ThanhTien, sum(ThanhTienThucchayKM) TienKM
		FROM ThucChay_Native_Ads tc
		where tc.TypeProduct = @TypeProduct 
		and SoHopDong not in ('HD_DEMO','','TONGSANPHAM')
		and NgayThucHien <=@NgayThucHien
		GROUP BY tc.Sohopdong
		)TC

		left join (
		select SoHopDong,ThoiGianSuaHopDong, sum(tthd)tthd, sum(tthdkm)tthdkm from (
		select SoHopDong, hd.LastModifiedAt ThoiGianSuaHopDong,
		(case when (hdct.ChietKhau = 100 or hdct.IsKhuyenMai = 1) then 0 else sum(hdct.ThanhTien) end ) tthd,
		(case when (hdct.ChietKhau = 100 or hdct.IsKhuyenMai = 1) then sum(hdct.SoLuong*hdct.DonGia) else 0 end ) tthdkm 
		from HopDong hd inner join HopDongChiTiet hdct on HopDongID =HopDongFK
		where 1=1 and hdct.DmSanPhamREF = @DmSanPhamREF and hdct.DeletedStatus =0
		and DmLoaiBannerREF not in (17,18) and DmLoaiREF <> 13
		--and SoHopDong ='QC7441118'
		group by SoHopDong,ChietKhau,IsKhuyenMai, hd.LastModifiedAt
		)h group by SoHopDong,ThoiGianSuaHopDong)HD
		on TC.SoHopDong =HD.SoHopDong
)A

full outer join 
(
select HopDongID, SoHopDong, round(sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0)tc, sum(ThanhTienKM+GiaTriKMThayDoi)km--, DonViTinh 
from thucchaydatinh where DmSanPhamREF = @DmSanPhamREF
and not (DmHinhThucQuangCao in (13) or DmLoaiBannerREF in (17, 18))
and len(dmbannerref) = 6
and NgayThucHien <=@NgayThucHien
group by SoHopDong, HopDongID
)B
on A.SoHopDong =B.SoHopDong
)A1
where A1.SoHopDong is null or A1.shd is null or 
abs (isnull(lechtc,0) -isnull(lechkm,0)) > 100
order by A1.ThoiGianSuaHopDong desc
END
/*
1. OnImage
QC3180820: hd có 2 pbo, đã đúng
QC7121120: ghi nhận theo mail
2. Native:

qc3120121: có 2 pbo, đã đúng
QC4401220: có 3 pbo, đã đúng
qc2651120: có 3 pbo, đã đúng
qc1711120
QC6711020
QC6471020
QC6201020
QC4311020
QC4221020
NB0041020
QC5530920
QC4970920
QC6940820
QC4020820
qc4900720
QC3870720
QC3380620
NB0380520
qc0400520
NB0270420
qc5300320: ghi nhận theo mail
QC0620320
NB0090120
QC0980120
*/
```
