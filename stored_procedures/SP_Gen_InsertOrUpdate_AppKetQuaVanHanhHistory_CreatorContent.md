# Stored Procedure: `Gen_InsertOrUpdate_AppKetQuaVanHanhHistory_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-01-05 11:01:49.590000
- **Ngày sửa cuối**: 2022-01-05 11:04:48.890000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_AppKetQuaVanHanhHistory_CreatorContent]

*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_AppKetQuaVanHanhHistory_CreatorContent] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = '''',
	@server_id_contract nvarchar(100) = '', @database_contract nvarchar(100) = ''
	SET @NgayThucHien = 
		ISNULL((
			SELECT  MAX(kq.[LastModificationTime])
			FROM   dbo.[AppKetQuaVanHanhHistory_CreatorContent] kq
		),'2017-01-01')

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CREATORCONTENT' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CREATORCONTENT' ORDER BY id),'')

	SET @server_id_contract =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @database_contract= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

	PRINT @NgayThucHien

	CREATE TABLE #AppKetQuaVanHanhHistory_CreatorContent(
			[Id] [INT] NOT NULL,
	[HopDongBanRef] [INT] NULL,
	[PhanBoRef] [INT] NULL,
	[PbSoLuong] [INT] NULL,
	[pbDonGia] [DECIMAL](18, 2) NULL,
	[PbChietKhau] [DECIMAL](18, 2) NULL,
	[PbThanhTien] [DECIMAL](18, 2) NULL,
	[AppHopDongKolCkTuNgay] [DATETIME] NULL,
	[AppHopDongKolCkDenNgay] [DATETIME] NULL,
	[NgayThucHien] [DATETIME] NULL,
	[Link] [NVARCHAR](2500) NULL,
	[TcDonViTinh] [INT] NULL,
	[TcSoLuong] [INT] NULL,
	[TcDonGia] [DECIMAL](18, 2) NULL,
	[TcThanhTien] [DECIMAL](18, 2) NULL,
	[AppPageKolRef] [INT] NULL,
	[AppHangMucRef] [INT] NULL,
	[AppHopDongKolRef] [INT] NULL,
	[DonGia] [DECIMAL](18, 2) NULL,
	[ChietKhau] [DECIMAL](18, 2) NULL,
	[TongTienGoc] [DECIMAL](18, 2) NULL,
	[TongTienDaThanhToan] [DECIMAL](18, 2) NULL,
	[ThanhTien] [DECIMAL](18, 2) NULL,
	[VAT] [DECIMAL](8, 2) NULL,
	[TienThanhToan] [DECIMAL](18, 2) NULL,
	[LaiLo] [DECIMAL](18, 2) NULL,
	[TrangThai] [TINYINT] NULL,
	[NguoiDuyet] [INT] NULL,
	[NgayDuyet] [DATETIME] NULL,
	[NguoiDuyetTT] [INT] NULL,
	[NgayDuyetTT] [DATETIME] NULL,
	[NguoiTuChoi] [INT] NULL,
	[NgayTuChoi] [DATETIME] NULL,
	[LyDoTuChoi] [NVARCHAR](500) NULL,
	[NguoiTuChoiTT] [INT] NULL,
	[NgayTuChoiTT] [DATETIME] NULL,
	[LyDoTuChoiTT] [NVARCHAR](500) NULL,
	[CreationTime] [DATETIME2](7) NULL,
	[CreatorUserId] [BIGINT] NULL,
	[NgayGuiDuyet] [DATETIME] NULL,
	[NguoiGuiDuyet] [INT] NULL,
	[NgayGuiDuyetTT] [DATETIME] NULL,
	[NguoiGuiDuyetTT] [INT] NULL,
	[isTongCk] [TINYINT] NULL,
	[AppKetQuaVanHanh_CreatorContentRef] [INT] NULL,
	[NgayThucHienTinhLaiCk] [DATETIME] NULL,
	[NguoiThucHienTinhLaiCk] [NVARCHAR](250) NULL,
	[ChietKhauQuyetToan] [DECIMAL](18, 2) NULL,
	[ThanhTienQuyetToan] [DECIMAL](18, 2) NULL,
	[LaiLoQuyetToan] [DECIMAL](18, 2) NULL,
	[NguoiDuyetTen] [NVARCHAR](250) NULL,
	[NguoiDuyetTTTen] [NVARCHAR](250) NULL,
	[NguoiTuChoiTen] [NVARCHAR](250) NULL,
	[NguoiTuChoiTTTen] [NVARCHAR](250) NULL,
	[CreatorUserName] [NVARCHAR](250) NULL,
	[LastModificationTime] [DATETIME2](7) NULL,
	[LastModifierUserName] [NVARCHAR](250) NULL,
	[LastModifierUserId] [BIGINT] NULL,
	[DeletionTime] [DATETIME2](7) NULL,
	[DeleterUserId] [BIGINT] NULL,
	[IsDeleted] [BIT] NULL,
	[NguoiGuiDuyetTen] [NVARCHAR](250) NULL,
	[NguoiGuiDuyetTTTen] [NVARCHAR](250) NULL,
	[TenAccSanPham] [NVARCHAR](250) NULL,
	[AccSanPham] [INT] NULL,
	[GhiChuKqvh] [NVARCHAR](500) NULL,
	[Version] [INT] NULL,
	[IsChiPhiPhatSinh] [BIT] NULL,
	[PageKolVanHanh] [INT] NULL,
	[Record_Status] smallint)

	SET @SQL = 
	'INSERT INTO #AppKetQuaVanHanhHistory_CreatorContent '

	SET @SQL +=
	'SELECT [Id]
      ,[HopDongBanRef]
      ,[PhanBoRef]
      ,[PbSoLuong]
      ,[pbDonGia]
      ,[PbChietKhau]
      ,[PbThanhTien]
      ,[AppHopDongKolCkTuNgay]
      ,[AppHopDongKolCkDenNgay]
      ,[NgayThucHien]
      ,[Link]
      ,[TcDonViTinh]
      ,[TcSoLuong]
      ,[TcDonGia]
      ,[TcThanhTien]
      ,[AppPageKolRef]
      ,[AppHangMucRef]
      ,[AppHopDongKolRef]
      ,[DonGia]
      ,[ChietKhau]
      ,[TongTienGoc]
      ,[TongTienDaThanhToan]
      ,[ThanhTien]
      ,[VAT]
      ,[TienThanhToan]
      ,[LaiLo]
      ,[TrangThai]
      ,[NguoiDuyet]
      ,[NgayDuyet]
      ,[NguoiDuyetTT]
      ,[NgayDuyetTT]
      ,[NguoiTuChoi]
      ,[NgayTuChoi]
      ,[LyDoTuChoi]
      ,[NguoiTuChoiTT]
      ,[NgayTuChoiTT]
      ,[LyDoTuChoiTT]
      ,[CreationTime]
      ,[CreatorUserId]
      ,[NgayGuiDuyet]
      ,[NguoiGuiDuyet]
      ,[NgayGuiDuyetTT]
      ,[NguoiGuiDuyetTT]
      ,[isTongCk]
      ,[idRef] AS [AppKetQuaVanHanh_CreatorContentRef]
      ,[NgayThucHienTinhLaiCk]
      ,[NguoiThucHienTinhLaiCk]
      ,[ChietKhauQuyetToan]
      ,[ThanhTienQuyetToan]
      ,[LaiLoQuyetToan]
      ,[NguoiDuyetTen]
      ,[NguoiDuyetTTTen]
      ,[NguoiTuChoiTen]
      ,[NguoiTuChoiTTTen]
      ,[CreatorUserName]
      ,[LastModificationTime]
      ,[LastModifierUserName]
      ,[LastModifierUserId]
      ,[DeletionTime]
      ,[DeleterUserId]
      ,[IsDeleted]
      ,[NguoiGuiDuyetTen]
      ,[NguoiGuiDuyetTTTen]
      ,[TenAccSanPham]
      ,[AccSanPham]
      ,[GhiChuKqvh]
      ,[Version]
      ,[IsChiPhiPhatSinh]
      ,[PageKolVanHanh]
	  ,0 [Record_Status]
	  FROM ' + @server_id + '.' + @database + '.[dbo].[AppKetQuaVanHanhHistory]
	  WHERE LastModificationTime >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '
				
	--PRINT @SQL
	EXEC(@SQL)

	UPDATE t 
	SET   t.[Record_Status] = 1
	FROM  #AppKetQuaVanHanhHistory_CreatorContent t INNER JOIN dbo.AppKetQuaVanHanhHistory_CreatorContent dc
	ON t.Id = dc.Id


	-- Insert Row chua ton tai
	INSERT INTO [dbo].[AppKetQuaVanHanhHistory_CreatorContent]
           ([Id]
           ,[HopDongBanRef]
           ,[PhanBoRef]
           ,[PbSoLuong]
           ,[pbDonGia]
           ,[PbChietKhau]
           ,[PbThanhTien]
           ,[AppHopDongKolCkTuNgay]
           ,[AppHopDongKolCkDenNgay]
           ,[NgayThucHien]
           ,[Link]
           ,[TcDonViTinh]
           ,[TcSoLuong]
           ,[TcDonGia]
           ,[TcThanhTien]
           ,[AppPageKolRef]
           ,[AppHangMucRef]
           ,[AppHopDongKolRef]
           ,[DonGia]
           ,[ChietKhau]
           ,[TongTienGoc]
           ,[TongTienDaThanhToan]
           ,[ThanhTien]
           ,[VAT]
           ,[TienThanhToan]
           ,[LaiLo]
           ,[TrangThai]
           ,[NguoiDuyet]
           ,[NgayDuyet]
           ,[NguoiDuyetTT]
           ,[NgayDuyetTT]
           ,[NguoiTuChoi]
           ,[NgayTuChoi]
           ,[LyDoTuChoi]
           ,[NguoiTuChoiTT]
           ,[NgayTuChoiTT]
           ,[LyDoTuChoiTT]
           ,[CreationTime]
           ,[CreatorUserId]
           ,[NgayGuiDuyet]
           ,[NguoiGuiDuyet]
           ,[NgayGuiDuyetTT]
           ,[NguoiGuiDuyetTT]
           ,[isTongCk]
           ,[AppKetQuaVanHanh_CreatorContentRef]
           ,[NgayThucHienTinhLaiCk]
           ,[NguoiThucHienTinhLaiCk]
           ,[ChietKhauQuyetToan]
           ,[ThanhTienQuyetToan]
           ,[LaiLoQuyetToan]
           ,[NguoiDuyetTen]
           ,[NguoiDuyetTTTen]
           ,[NguoiTuChoiTen]
           ,[NguoiTuChoiTTTen]
           ,[CreatorUserName]
           ,[LastModificationTime]
           ,[LastModifierUserName]
           ,[LastModifierUserId]
           ,[DeletionTime]
           ,[DeleterUserId]
           ,[IsDeleted]
           ,[NguoiGuiDuyetTen]
           ,[NguoiGuiDuyetTTTen]
           ,[TenAccSanPham]
           ,[AccSanPham]
           ,[GhiChuKqvh]
           ,[Version]
           ,[IsChiPhiPhatSinh]
           ,[PageKolVanHanh])
    
	SELECT [Id]
		  ,[HopDongBanRef]
		  ,[PhanBoRef]
		  ,[PbSoLuong]
		  ,[pbDonGia]
		  ,[PbChietKhau]
		  ,[PbThanhTien]
		  ,[AppHopDongKolCkTuNgay]
		  ,[AppHopDongKolCkDenNgay]
		  ,[NgayThucHien]
		  ,[Link]
		  ,[TcDonViTinh]
		  ,[TcSoLuong]
		  ,[TcDonGia]
		  ,[TcThanhTien]
		  ,[AppPageKolRef]
		  ,[AppHangMucRef]
		  ,[AppHopDongKolRef]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[TongTienGoc]
		  ,[TongTienDaThanhToan]
		  ,[ThanhTien]
		  ,[VAT]
		  ,[TienThanhToan]
		  ,[LaiLo]
		  ,[TrangThai]
		  ,[NguoiDuyet]
		  ,[NgayDuyet]
		  ,[NguoiDuyetTT]
		  ,[NgayDuyetTT]
		  ,[NguoiTuChoi]
		  ,[NgayTuChoi]
		  ,[LyDoTuChoi]
		  ,[NguoiTuChoiTT]
		  ,[NgayTuChoiTT]
		  ,[LyDoTuChoiTT]
		  ,[CreationTime]
		  ,[CreatorUserId]
		  ,[NgayGuiDuyet]
		  ,[NguoiGuiDuyet]
		  ,[NgayGuiDuyetTT]
		  ,[NguoiGuiDuyetTT]
		  ,[isTongCk]
		  ,[AppKetQuaVanHanh_CreatorContentRef]
		  ,[NgayThucHienTinhLaiCk]
		  ,[NguoiThucHienTinhLaiCk]
		  ,[ChietKhauQuyetToan]
		  ,[ThanhTienQuyetToan]
		  ,[LaiLoQuyetToan]
		  ,[NguoiDuyetTen]
		  ,[NguoiDuyetTTTen]
		  ,[NguoiTuChoiTen]
		  ,[NguoiTuChoiTTTen]
		  ,[CreatorUserName]
		  ,[LastModificationTime]
		  ,[LastModifierUserName]
		  ,[LastModifierUserId]
		  ,[DeletionTime]
		  ,[DeleterUserId]
		  ,[IsDeleted]
		  ,[NguoiGuiDuyetTen]
		  ,[NguoiGuiDuyetTTTen]
		  ,[TenAccSanPham]
		  ,[AccSanPham]
		  ,[GhiChuKqvh]
		  ,[Version]
		  ,[IsChiPhiPhatSinh]
		  ,[PageKolVanHanh]
	  FROM #AppKetQuaVanHanhHistory_CreatorContent
	  WHERE Record_Status = 0 --trang thai ban ghi cho viec syn du lieu

	DROP TABLE #AppKetQuaVanHanhHistory_CreatorContent
END

--select * from dbo.AppKetQuaVanHanhHistory_CreatorContent
```
