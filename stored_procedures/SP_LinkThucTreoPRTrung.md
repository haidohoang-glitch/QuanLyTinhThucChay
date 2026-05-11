# Stored Procedure: `LinkThucTreoPRTrung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-13 17:57:49.193000
- **Ngày sửa cuối**: 2019-05-27 10:05:18.650000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[LinkThucTreoPRTrung] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
		SET NOCOUNT ON;
    -- Insert statements for procedure here
	delete from ListLinkThucTreoPRTrung
Insert into ListLinkThucTreoPRTrung
	select getdate()NgayCanhBao, A.HopDongREF,A.SoHopDong, A.Link, A.GhiChu, count(*)SoLanLap from (
	SELECT HopDongREF, dbo.GetSoHopDongByID(HopDongREF)SoHopDOng, Link,isnull(GhiChu,'')GhiChu 
	from ThucChayHopDongChiTietPR
	where DeletedStatus = 0 
	and isnull(link,'') <>''
	)A
	where right(SoHopDong,2)>='18'	
	and A.SoHopDong not in ('SH0060318','SH0040818','SH0050718','SH0060618','SH0050418','SH0061018','QC3781018','NB0100718')
	
	group by A.HopDongREF,A.SoHopDong, A.link, A.ghichu
	having count(*) > 1
	order by HopDongREF desc

	select  NgayCanhBao,SoHopDong, Link, GhiChu,SoLanLap from ListLinkThucTreoPRTrung
	where convert(date,NgayCanhBao) = convert(date,getdate())

END
/* ThucTreo
select  NgayCanhBao,SoHopDong, Link, GhiChu,SoLanLap from ListLinkThucTreoPRTrung
select A.contract_id,A.Contract_Number, A.link, A.ghichu, count(*)solanlap from (
	SELECT contract_id,Contract_Number, link,isnull(ghichu,'')ghichu from ThucTreo_PR
	where Deleted_Status = 0 
	and isnull(link,'') <>''
	and RIGHT(contract_number,2)>='18'	
	and Contract_Number not in ('SH0060318','SH0040818','SH0050718','SH0060618','SH0050418','SH0061018','QC3781018')
	)A
	group by A.contract_id,A.Contract_Number, A.link, A.ghichu
	having count(*) > 1
	order by contract_id desc

	-- lap link ở các so hop dong khac nhau
	Declare @table table (link nvarchar(500), solanlap int)
	insert into @table
	SELECT link,count(*) solanlap from ThucChayHopDongChiTietPR
	where DeletedStatus = 0 
	and isnull(link,'') <>''	
	and RIGHT(dbo.GetSoHopDongByID(HopDongREF),2) >='18'
	and dbo.GetSoHopDongByID(HopDongREF) not in ('SH0060318','SH0040818','SH0050718','SH0060618','SH0050418','SH0061018','QC3781018')	
	group by link
	having count(*) > 1
	
	select A.link, A.SoHopDong, A.SoLanLap, A.GhiChu from (
	select distinct dbo.GetSoHopDongByID(HopDongREF)SoHopDong,a.Link, GhiChu,b.solanlap
	from ThucChayHopDongChiTietPR a
	 inner join @table b on a.Link = b.link 
	 )A order by A.link, A.SoHopDong


	 Declare @table table (link nvarchar(500), solanlap int)
	insert into @table
	SELECT link,count(*) solanlap from ThucTreo.dbo.ThucTreo_PR
	where Deleted_Status = 0 
	and isnull(link,'') <>''	
	and RIGHT(Contract_Number,2) >='18'
	and Contract_Number not in ('SH0060318','SH0040818','SH0050718','SH0060618','SH0050418','SH0061018','QC3781018')	
	group by link
	having count(*) > 1
	
	select A.link, A.SoHopDong, A.SoLanLap, A.GhiChu from (
	select distinct Contract_Number SoHopDong,a.Link, GhiChu,b.solanlap
	from ThucTreo.dbo.ThucTreo_PR a
	 inner join @table b on a.Link = b.link 
	 )A order by A.link, A.SoHopDong
	*/
	

	
```
