# Stored Procedure: `sp_KSTC_CheckIbiz`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-29 11:36:52.760000
- **Ngày sửa cuối**: 2021-06-07 09:28:34.617000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckIbiz]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

declare @FromDate datetime,@ToDate datetime,
@gross float,@grossIBiz float,
@tcb float,@tcbIbiz float,
@chenhlech float,@chenhlechIbiz float,
@mn float,@mnIbiz float,@ggfb float,@ggfbIbiz float,
@chenhlechggfb float,@chenhlechggfbIbiz float

set @ToDate = (select  MAX(ACTUAL_RUN_DATE) from [ASD14].contract.dbo.CONTRACT_INFO_DATE_RUNNING_REAL)
set @FromDate = convert(date,(SELECT CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(@ToDate)-1),@ToDate),101)))

--1. Số tổng Gross
set @gross = (select sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) 
from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh
where NgayThucHien between @FromDate and @ToDate
and TenMaHopDong not in ('NB','NBDT')
)

set @grossIBiz = (select sum(DoanhSoThucChay) 
from [asd14].BI_SmartPhone.dbo.NhanHang_DoanhSoThucChayChiTiet
where NgayThucHien between @FromDate and @ToDate
)
--2. Số TCBNB không gồm Mua ngoài và GGFB
set @tcb = (select sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) 
from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh
where NgayThucHien between @FromDate and @ToDate
and not( DmHinhThucQuangCao = 13 or DmLoaiBannerREF = 18 )
and not (DmSanPhamREF in (306,423) or DmBannerREF  in (100093,100478))
and TenMaHopDong not in ('NB','NBDT')
)

set @tcbIbiz = (select sum(DoanhSoThucChay) 
from [asd14].BI_SmartPhone.dbo.NhanHang_DoanhSoThucChayChiTiet
where NgayThucHien between @FromDate and @ToDate
and not( DmHinhThucQuangCaoREF = 13 or DmLoaiBannerREF = 18 )
and not (DmSanPhamREF in (306,423) or DmBannerREF  in (100093,100478))
)


--2. TCMN
set @mn = (select sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) 
from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh
where NgayThucHien between @FromDate and @ToDate
and ( DmHinhThucQuangCao = 13 or DmLoaiBannerREF = 18)
and TenMaHopDong not in ('NB','NBDT')
)


set @mnIbiz = (select sum(DoanhSoThucChay) 
from [asd14].BI_SmartPhone.dbo.NhanHang_DoanhSoThucChayChiTiet
where NgayThucHien between @FromDate and @ToDate
and ( DmHinhThucQuangCaoREF = 13 or DmLoaiBannerREF = 18 )
)

--2. TCGGFB
set @ggfb = (select sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) 
from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh
where NgayThucHien between @FromDate and @ToDate
and (DmSanPhamREF in (306,423) or DmBannerREF  in (100093,100478))
and TenMaHopDong not in ('NB','NBDT')
)

set @ggfbIbiz = (select sum(DoanhSoThucChay) 
from [asd14].BI_SmartPhone.dbo.NhanHang_DoanhSoThucChayChiTiet
where NgayThucHien between @FromDate and @ToDate
and (DmSanPhamREF in (306,423) or DmBannerREF  in (100093,100478))
)

--3.Số chênh lệch bán mua (MN)
set @chenhlech = (select  sum(GiaTriThayDoiLaiSauCK+ThanhTienLaiThucChaySauCK) 
from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh_MuaNgoai
where NgayThucHien between @FromDate and @ToDate
and ( DmHinhThucQuangCaoREF = 13 or DmLoaiBannerREF = 18)
and DmMaHopDongREF not in (345,310)
)
set @chenhlechIbiz = (select sum(LaiMuaNgoai) MN
from [asd14].[BI_SmartPhone].dbo.NhanHang_DoanhSoThucChay_MuaNgoaiChiTiet
where NgayThucHien between @FromDate and @ToDate
and (DmHinhThucQuangCaoREF = 13 or DmLoaiBannerREF = 18)
)

set @chenhlechggfb = (select  sum(GiaTriThayDoiLaiSauCK+ThanhTienLaiThucChaySauCK) 
from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh_MuaNgoai
where NgayThucHien between @FromDate and @ToDate
and (DmSanPhamREF in (306,423) or DmBannerREF  in (100093,100478))
and DmMaHopDongREF not in (345,310)
)
set @chenhlechggfbIbiz = (select sum(LaiMuaNgoai) LaiGGFB
from [asd14].[BI_SmartPhone].dbo.NhanHang_DoanhSoThucChay_GoogleFacebookChiTiet
where NgayThucHien between @FromDate and @ToDate
)

Declare @table Table
(Tenbang nvarchar(50)
,DuLieuChotDenNgay nvarchar(50)
,gross nvarchar(50)
,mn nvarchar(50)
,chenhlech nvarchar(50)
,NET nvarchar(50)
)
Insert into @table
select
'ABM',(select convert(Date,max(NgayThucHien)) from [asd14].ABM_Data_Release.dbo.ThucChayDaTinh)DuLieuChotDenNgay,
dbo.FormatNumber(@gross)gross,
dbo.FormatNumber(@mn)mn,
dbo.FormatNumber(@chenhlech)chenhlech, 
dbo.FormatNumber((@gross - @mn - @ggfb) + @chenhlech + @chenhlechggfb) NET
Insert into @table
select 'IBiz',(select convert(Date,max(NgayThucHien)) from [asd14].BI_SmartPhone.dbo.NhanHang_DoanhSoThucChayChiTiet)DuLieuChotDenNgay,

dbo.FormatNumber(@grossIBiz) grossIBiz,
dbo.FormatNumber(@mnIbiz)mnIbiz,
dbo.FormatNumber(@chenhlechIbiz)chenhlechIbiz,
dbo.FormatNumber((@grossIBiz - @mnIbiz- @ggfbIbiz) + @chenhlechIbiz +@chenhlechggfbIbiz) NETIbiz

select * from @Table
END

```
