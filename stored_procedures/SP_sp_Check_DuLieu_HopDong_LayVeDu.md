# Stored Procedure: `sp_Check_DuLieu_HopDong_LayVeDu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-21 11:54:55.927000
- **Ngày sửa cuối**: 2024-10-14 09:49:50.093000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
--modify by duongnt ngay 11/10/2024
-- =============================================
CREATE PROCEDURE [dbo].[sp_Check_DuLieu_HopDong_LayVeDu] 
	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
---Kiểm tra dữ liệu Hopdong, Hopdongchitiet với ThoiGian = getdate() -1
select N'Dữ liệu hợp đồng' Bảng, convert(date,lastmodifiedat) as DayCall , max(lastmodifiedat) as MaxTimeCall, count(*) as SoBanGhi from Hopdong where convert(date,lastmodifiedat) =  convert(date,getdate()-1) 
group by convert(date,lastmodifiedat)
union all
select N'contracts' Bảng, convert(date,LAST_MODIFIED_AT) as DayCall , max(LAST_MODIFIED_AT) as MaxTimeCall, count(*) as SoBanGhi from ASDAG2.CONTRACT.dbo.contracts where convert(date,LAST_MODIFIED_AT) =  convert(date,getdate()-1) AND STATUS<>0
group by convert(date,LAST_MODIFIED_AT)
union all
select N'Dữ liệu hợp đồng chi tiết' Bảng, convert(date,lastmodifiedat) as DayCall ,max(lastmodifiedat) as MaxTimeCall,  count(*) as SoBanGhi from Hopdongchitiet where convert(date,lastmodifiedat) = convert(date,getdate()-1)
group by CONVERT(date,lastmodifiedat)
union all
select N'CONTRACT_DETAILS' Bảng, convert(date,LAST_MODIFIED_AT) as DayCall , max(LAST_MODIFIED_AT) as MaxTimeCall, count(*) as SoBanGhi from ASDAG2.CONTRACT.dbo.CONTRACT_DETAILS where convert(date,LAST_MODIFIED_AT) =  convert(date,getdate()-1) 
--AND CONTRACT_ID NOT IN (SELECT ID from ASDAG2.CONTRACT.dbo.contracts where convert(date,LAST_MODIFIED_AT) =  convert(date,getdate()-1) AND STATUS=0) --loại phân bổ hđ nháp
group by convert(date,LAST_MODIFIED_AT)
union all
select N'Dữ liệu hợp đồng thay đổi' Bảng, convert(date,lastmodifiedat) as DayCall ,max(lastmodifiedat) as MaxTimeCall,  count(*) as SoBanGhi from Hopdongthaydoi where convert(date,lastmodifiedat) = convert(date,getdate()-1)
group by convert(date,lastmodifiedat)
union all
select N'CONTRACT_CHANGE' Bảng, convert(date,DATE_CHANGE) as DayCall , max(DATE_CHANGE) as MaxTimeCall, count(*) as SoBanGhi from ASDAG2.CONTRACT.dbo.CONTRACT_CHANGE where convert(date,DATE_CHANGE) =  convert(date,getdate()-1) 
group by convert(date,DATE_CHANGE)
union all
select N'Dữ liệu hợp đồng chi tiết thay đổi' Bảng, convert(date,lastmodifiedat) as DayCall ,max(lastmodifiedat) as MaxTimeCall,  count(*) as SoBanGhi from Hopdongchitietthaydoi where convert(date,lastmodifiedat) = convert(date,getdate()-1)
group by convert(date,lastmodifiedat)
union all
select N'CONTRACT_DETAIL_CHANGE' Bảng, convert(date,a.DATE_CHANGE) as DayCall , max(a.DATE_CHANGE) as MaxTimeCall, count(*) as SoBanGhi FROM ASDAG2.CONTRACT.dbo.CONTRACT_DETAIL_CHANGE c
 JOIN ASDAG2.CONTRACT.dbo.CONTRACT_CHANGE a ON a.ID = c.CONTRACT_CHANGE_ID
  WHERE convert(date,a.DATE_CHANGE) =  convert(date,getdate()-1)
group by convert(date,a.DATE_CHANGE)

END

```
