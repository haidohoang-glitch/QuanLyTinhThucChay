# Stored Procedure: `XuLy_DuLieu_ThucChayMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-01-02 16:10:47.757000
- **Ngày sửa cuối**: 2020-09-12 10:57:03.670000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC XuLy_DuLieu_ThucChayMuaNgoai
CREATE PROCEDURE [dbo].[XuLy_DuLieu_ThucChayMuaNgoai]

AS
BEGIN
	DECLARE @FromDate DATETIME, @ToDate DATETIME
	SET @FromDate = '2019-12-21'
	SET @ToDate = '2019-12-31'

--delete from ThucChayDaTinh 
--where HopDongID = 1018047 and DmSanPhamREF = 821

--delete from thucchaydatinh where  hopdongchitietref= 575932 and ngaythuchien ='2020-03-02'
--	and DotChayBooking = 10266 and GhiChu = 'DOI TRU MUA NGOAI, THAY DOI THANH TIEN THUC CHAY: 10266' and abs(giatrithaydoi) < 2349154
--delete from thucchaydatinh where  hopdongchitietref= 575932 and ngaythuchien ='2020-03-02'
--	and DotChayBooking = 10266 and GhiChu = 'DOI TRU MUA NGOAI, THAY DOI THANH TIEN THUC CHAY: 10266' and abs(giatrithaydoi) > 2350542

	/*
	select DotChayBooking, count(*) from thucchaydatinh where  hopdongchitietref= 575932 and ngaythuchien ='2020-03-02'
group by DotChayBooking
order by DotChayBooking

select  sum(ThanhTienSauTrietKhauThucChay), sum(GiaTriThayDoi) from thucchaydatinh where  hopdongchitietref= 575932
	and ngaythuchien ='2020-03-02' and DotChayBooking = 10266 and GhiChu = 'DOI TRU MUA NGOAI, THAY DOI THANH TIEN THUC CHAY: 10266'
	select  DotChayBooking,GiaTriThayDoi from thucchaydatinh where  hopdongchitietref= 575932 and ngaythuchien ='2020-03-02'
	and DotChayBooking = 10266 and GhiChu = 'DOI TRU MUA NGOAI, THAY DOI THANH TIEN THUC CHAY: 10266'
order by abs(GiaTriThayDoi) 

	
	

	select count (*), DmSanPhamREF,DmHinhThucQuangCao,SoHopDong,HopDongID, HopDongChiTietREF, NgayThucHien from ThucChayDaTinh where HopDongChiTietREF = 575932
group by SoHopDong,HopDongID,DmSanPhamREF,DmHinhThucQuangCao,NgayThucHien,HopDongChiTietREF
 order by  NgayThucHien desc
	512
10267	512
10268	512
10317	512
10318	512
10336	128
10337	128



*/
END


```
