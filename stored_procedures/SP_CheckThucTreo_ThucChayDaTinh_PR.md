# Stored Procedure: `CheckThucTreo_ThucChayDaTinh_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-09 15:01:04.667000
- **Ngày sửa cuối**: 2019-05-28 15:25:30.793000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[CheckThucTreo_ThucChayDaTinh_PR] 
	-- Add the parameters for the stored procedure here
	--@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @NgayThucHien datetime
	declare @ThucTreo_ThucChayDaTinh_PR_Now table
	(
	Ngay nvarchar(50),
	HopDongID_TT int,
	SoHopDong_TT nvarchar(50),
	DmSanPhamREF_TT int,
	Tien_TT float,
	HopDongID_TCDT int,
	SoHopDong_TCDT nvarchar(50),
	DmSanPhamREF_TCDT int,
	Tien_TCDT float,
	Lech_TCDT_TTT float
	)
	declare @ThucTreo_ThucChayDaTinh_PR_All table
	(
	Ngay nvarchar(50),
	HopDongID_TT int,
	SoHopDong_TT nvarchar(50),
	DmSanPhamREF_TT int,
	Tien_TT float,
	HopDongID_TCDT int,
	SoHopDong_TCDT nvarchar(50),
	DmSanPhamREF_TCDT int,
	Tien_TCDT float,
	Lech_TCDT_TTT float
	)
		delete from ThucTreo_ThucChayDaTinh_PR
		
		set @NgayThucHien = convert(date,dateadd(day, -1,getdate()))
		
		--select @NgayThucHien1 
		--chỉ tính ngày hiện tại
		insert into @ThucTreo_ThucChayDaTinh_PR_Now
		select  N'Now' Ngay, A.*,
		B.*, isnull(A.thuctreo,0) - isnull(B.tcdt,0)lech from (
		select hopdongref,dbo.getsohopdongbyid(hopdongref) shd,DmSanPhamREF, sum(soluong*giatien*(100-chietkhau)/100)thuctreo
		from ThucChayHopDongChiTietPR where DeletedStatus = 0
		--and HopDongref = 1007109
		and convert(date,LastModifiedAt) = @NgayThucHien
		and hopdongref in (select HopDongREF from ThucChayHopDongChiTietPR where convert(date,LastModifiedAt) = @NgayThucHien) 
		group by HopDongREF,DmSanPhamREF
		
		)A
		full outer join
		(
		select HopDongID,SoHopDong,DmSanPhamREF, sum(Thanhtiensautrietkhauthucchay+giatrithaydoi) tcdt
		 from thucchaydatinh
		 where DmSanPhamREF in (141,637,305) and not (DmLoaiBannerREF = 18 or DmHinhThucQuangCao = 13)
		and TrangThaiHopDong <> 3 and NgayThucHien = @NgayThucHien
		and (HopDongID in (select HopDongFK from hopdongchitiet where convert(date,LastModifiedAt) = @NgayThucHien)
		--or HopDongID in  (select HopDongID from HopDong where convert(date,LastModifiedAt) = @NgayThucHien)
		or  HopDongID in (select HopDongREF from ThucChayHopDongChiTietPR where convert(date,LastModifiedAt) = @NgayThucHien)
		 )
		--and HopDongid = 1007109
		group by HopDongID,SoHopDong,DmSanPhamREF
		)B
		on A.HopDongREF = B.HopDongID
		and A.DmSanPhamREF = B.DmSanPhamREF
		where abs(isnull(A.thuctreo,0) - isnull(B.tcdt,0)) > 5
		order by A.HopDongREF desc
		


		-- tính đến ngày hiện tại
		declare @table table
		(HopDongID int)
		declare @year int, @date datetime
		set @date = convert(datetime,'1/1/' + convert(nvarchar(10),year(getdate())))
		--select @date
		insert into @table 
		select distinct HopDongREF from ThucChayHopDongChiTietPR where LastModifiedAt >=@date
		and HopDongREF not in (select HopDongID from HopDong where TrangThaiHopDong = 3)

		insert into @ThucTreo_ThucChayDaTinh_PR_All
		select N'All ' + convert(nvarchar(50),@NgayThucHien,101), A.*,
		B.*, isnull(A.thuctreo,0) - isnull(B.tcdt,0)lech from (
		select hopdongref,dbo.getsohopdongbyid(hopdongref) shd,DmSanPhamREF, sum(soluong*giatien*(100-chietkhau)/100)thuctreo
		from ThucChayHopDongChiTietPR where DeletedStatus = 0
		--and HopDongref = 1007109
			and convert(date,LastModifiedAt) <= @NgayThucHien
		and RIGHT(dbo.getsohopdongbyid(hopdongref),2) >='17'
		and  hopdongref in (select HopDongID from @table) 
		
		group by HopDongREF,DmSanPhamREF
		
		)A
		full outer join
		(
		select HopDongID,SoHopDong,DmSanPhamREF, sum(Thanhtiensautrietkhauthucchay+giatrithaydoi) tcdt
		 from thucchaydatinh
		 where DmSanPhamREF in (141,637,305) and not (DmLoaiBannerREF = 18 or DmHinhThucQuangCao = 13)
		and TrangThaiHopDong <> 3
		and  HopDongID in (select HopDongID from @table) 
		and RIGHT(SoHopDong,2) >='17'
		group by HopDongID,SoHopDong,DmSanPhamREF
		)B
		on A.HopDongREF = B.HopDongID
		and A.DmSanPhamREF = B.DmSanPhamREF
		where abs(isnull(A.thuctreo,0) - isnull(B.tcdt,0)) > 5
		order by A.HopDongREF desc

		--select du lieu

		insert into ThucTreo_ThucChayDaTinh_PR 
		select * from @ThucTreo_ThucChayDaTinh_PR_Now where 
		(
		HopDongID_TT not in (select HopDongID_TT from @ThucTreo_ThucChayDaTinh_PR_All union all  select HopDongID_TCDT from @ThucTreo_ThucChayDaTinh_PR_All)
		or HopDongID_TCDT not in (select HopDongID_TT from @ThucTreo_ThucChayDaTinh_PR_All union all  select HopDongID_TCDT from @ThucTreo_ThucChayDaTinh_PR_All)
		)
		insert into ThucTreo_ThucChayDaTinh_PR 
		select * from @ThucTreo_ThucChayDaTinh_PR_All  
		
		
		select Ngay ,
	HopDongID_ThucTreo ,
	SoHopDong_ThucTreo,
	DmSanPhamREF_ThucTreo ,
	dbo.FormatNumber(Tien_ThucTreo)Tien_ThucTreo ,
	HopDongID_TCDT ,
	SoHopDong_TCDT ,
	DmSanPhamREF_TCDT ,
	dbo.FormatNumber(Tien_TCDT)Tien_TCDT ,
	dbo.FormatNumber(Lech_TCDT_ThucTreo) Lech_TCDT_ThucTreo
	from ThucTreo_ThucChayDaTinh_PR
	order by HopDongID_ThucTreo desc,HopDongID_TCDT desc
	 
END

```
